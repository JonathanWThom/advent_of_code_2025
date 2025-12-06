from functools import reduce, cache

class LineGetter:
    def __init__(self, path):
        self.path = path

    def lines(self):
        return open(self.path).read().split("\n")[:-1]

class Homework:
    def __init__(self):
        self.path = "./day6_input.txt"

    def solve(self):
        grand_total = 0
        for collection in self._collections():
            operator = collection.pop()
            grand_total += reduce(lambda x, y: eval(f"{x} {operator} {y}"), collection)

        print(grand_total)
        return grand_total

    def _collections(self):
        collections = []
        for i in range(0, len(self._filtered_lines()[0])):
            collection = []
            for split in self._filtered_lines():
                collection.append(split[i])
            collections.append(collection)

        return collections

    @cache
    def _filtered_lines(self):
        def no_empties(line):
            return list(filter(None, line.split(" ")))

        return list(map(no_empties, self._lines()))

    def _lines(self):
        return LineGetter(self.path).lines()

Homework().solve()
