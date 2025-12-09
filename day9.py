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
        self.matches = []

class Floor:
    def __init__(self, width, depth, lines):
        self.width = width
        self.depth = depth
        self.red_tiles = []
        self.tiles = self._build_tiles(lines)

    def _build_tiles(self, lines):
        tmp = dict()

        for line in lines:
            x, y = line.split(",")
            tile = Tile(int(x), int(y))
            if tmp.get(int(x)) == None:
                tmp[int(x)] = {}
            tmp[int(x)][int(y)] = tile
            self.red_tiles.append(tile)

        return tmp

    def get_best_rectangle_for(self, tile):
        areas = []

        for i, red_tile in enumerate(self.red_tiles):
            if red_tile == tile:
                continue

            x_magnitude = abs(red_tile.x - tile.x)+1
            y_magnitude = abs(red_tile.y - tile.y)+1
            area = x_magnitude * y_magnitude
            areas.append(area)

        if len(areas) == 0:
            return 0

        return max(areas)

f=Floor(width, depth, lines)
for tile in f.red_tiles:
    areas.append(f.get_best_rectangle_for(tile))

print(max(areas))
