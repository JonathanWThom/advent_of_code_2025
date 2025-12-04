class Grid:
    def __init__(self, lines):
        self.lines = lines
        self.lookup = {}
        self.squares = self._build_squares()

    def _build_squares(self):
        squares = []
        for y, line in enumerate(self.lines):
            for x, sq in enumerate(list(line)):
                square = Square(sq, x, y)
                squares.append(square)
                self.lookup[x, y] = square

        return squares

    def get_accessible_squares(self):
        accessible = 0
        for square in self.squares:
            if not square.is_roll():
                continue
            count = square.get_roll_neighbors_count(self.lookup)
            if count < 4:
                accessible += 1

        print(accessible)
        return accessible




class Square:
    def __init__(self, value, x, y):
        self.x = x
        self.y = y
        self.value = value

    def is_roll(self):
        return self.value == "@"

    def get_roll_neighbors_count(self, lookup):
        # (x-1, y+1) (x, y+1) (x+1, y+1)
        # (x-1, y)   (x,y) (x+1, y)
        # (x-1, y-1) (x, y-1) (x+1, y-1)
        neighbors = [
            [self.x - 1, self.y+1],
            [self.x, self.y+1],
            [self.x+1, self.y+1],
            [self.x-1, self.y],
            [self.x+1, self.y],
            [self.x-1, self.y-1],
            [self.x, self.y-1],
            [self.x+1, self.y-1]
        ]

        count = 0
        for neighbor in neighbors:
            square = lookup.get((neighbor[0], neighbor[1]))
            if square is not None and square.is_roll():
                count += 1

        return count

lines = open("./day4_input.txt").read().split("\n")[:-1]
Grid(lines).get_accessible_squares()
