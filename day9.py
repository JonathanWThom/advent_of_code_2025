lines = open("./day9_input.txt").read().splitlines()

def x(line):
    return int(line.split(",")[0])

def y(line):
    return int(line.split(",")[1])

width = max(list(map(x, lines)))
depth = max(map(y, lines))
areas = []

class Tile:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.red = False

class Floor:
    def __init__(self, width, depth, lines):
        self.width = width
        self.depth = depth
        self.red_tiles = []
        self.tiles = self._build_tiles(lines)

    def _build_tiles(self, lines):
        tmp = dict()
        for x in range(width+1):
            tmp[x] = {}
            for y in range(depth+1):
                tmp[x][y] = Tile(x, y)

        for line in lines:
            x, y = line.split(",")
            tile = tmp[int(x)][int(y)]
            tile.red = True
            self.red_tiles.append(tile)

        return tmp

    def get_best_rectangle_for(self, tile):
        areas = []

        for red_tile in self.red_tiles:
            if red_tile == tile:
                continue
            x_magnitude = abs(red_tile.x - tile.x)+1
            y_magnitude = abs(red_tile.y - tile.y)+1
            area = x_magnitude * y_magnitude
            areas.append(area)

        return max(areas)

f=Floor(width, depth, lines)
for tile in f.red_tiles:
    areas.append(f.get_best_rectangle_for(tile))

print(max(areas))
