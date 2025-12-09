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

        # horizontal
        for x in range(0, self.width+1): # +2?
            if x == tile.x:
                continue
            if self.tiles[x][tile.y].red == True:
                area = abs(x-tile.x)+1
                print(f"tile at [{x}, {tile.y}] forms rectangle with [{tile.x}, {tile.y}] with area: {area}")
                areas.append(area)

        # vertical
        for y in range(0, self.depth+1): # +2?
            if y == tile.y:
                continue

            if self.tiles[tile.x][y].red == True:
                area = abs(y-tile.y)+1
                print(f"tile at [{tile.x}, {y}] forms rectangle with [{tile.x}, {tile.y}] with area: {area}")
                areas.append(area)

        # up right diagonally: wrong algo
        for x in range(tile.x+1, self.width+1): # move to the right starting at tile until reaching end
            current_y =
            # for each move to the right, you have to subtract 1 from tile.y
            if tile.x == 2 and tile.y == 5:
                if x == 11:
                    print("current_y", current_y)

            if self.tiles.get(x, {}).get(current_y, Tile(-1,-1)).red == True:
                x_move = abs(x-tile.x)+1
                y_move = abs(curren_y-tile.y)+1
                area = x_move * y_move
                print(f"tile at [{x}, {current_y}] forms rectangle with [{tile.x}, {tile.y}] with area: {area}")
                areas.append(area)

        # down right diagonally: wrong algo
        for x in range(tile.x, self.width+1): # move to the right starting at tile until reaching end
            # for each move to the right, you have to add 1 to tile.y
            current_y = tile.y + 1
            if self.tiles.get(x, {}).get(current_y, Tile(-1,-1)).red == True:
                x_move = abs(x-tile.x)+1
                y_move = abs(curren_y-tile.y)+1
                area = x_move * y_move
                print(f"tile at [{x}, {current_y}] forms rectangle with [{tile.x}, {tile.y}] with area: {area}")
                areas.append(area)

        return max(areas)

f=Floor(width, depth, lines)
print(len(f.red_tiles))
for tile in f.red_tiles:
    areas.append(f.get_best_rectangle_for(tile))

# rules about what coordinates form triangles with a coordinate
# [0,0] [1,0] [2,0] [3,0] [4,0]
# [0,1] [1,1] [2,1] [3,1] [4,1]
# [0,2] [1,2] [2,2] [3,2] [4,2]
# [0,3] [1,3] [2,3] [3,3] [4,3]
# [0,4] [1,4] [2,4] [3,4] [4,4]

# NO this is the wrong idea, it doesn't follow these 1 up, 1 to the side rules
# for [2,2], possible thin rectangles are
# anything with same y value that are not it: [0,2] [1,2] [3,2] [4,2]
# anything with same x value that is not it: [2,0] [2,1] [2,3] [2,4]
# up right diagonally: [3, 1] [4,0]
# down right diagonally: [3, 3] [4,4]
# down left diagonally: [1,3] [0,4]
# up left diagonally: [1,1] [0,0]

# fill in the floor with max x and max y in a dict
# then go through and mark certain tiles as red (maybe make dict too?), or just
# a list
# then for each red tile, check its possible rectangles in the floor to see if
# they are also red
# if they are, get the area
# collect all areas and get the max
print(max(areas))
