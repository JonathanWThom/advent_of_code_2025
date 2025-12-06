from functools import reduce

lines = open("./day6_input.txt").read().split("\n")[:-1]
split_lines = []
for line in lines:
    split = list(filter(None, line.split(" ")))
    split_lines.append(split)

collections = []
for i in range(0, len(split_lines[0])):
    collection = []
    for split in split_lines:
        collection.append(split[i])
    collections.append(collection)

grand_total = 0
for collection in collections:
    operator = collection.pop()
    grand_total += reduce(lambda x, y: eval(f"{x} {operator} {y}"), collection)

print(grand_total)
