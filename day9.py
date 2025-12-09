lines = open("./day9_input.txt").read().splitlines()

areas = []

class Tile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Floor:
    def __init__(self, lines):
        self.red_tiles = self._build_tiles(lines)

    def _build_tiles(self, lines):
        tmp = []
        for line in lines:
            x, y = line.split(",")
            tile = Tile(int(x), int(y))
            tmp.append(tile)

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

        if len(areas) == 0:
            return 0

        return max(areas)

f=Floor(lines)
for tile in f.red_tiles:
    areas.append(f.get_best_rectangle_for(tile))

print(max(areas))
