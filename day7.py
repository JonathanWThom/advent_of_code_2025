splits = 0
lines = open("./day7_input.txt").read().splitlines()
generations = []
for l in lines:
    generations.append(list(l))

for i, generation in enumerate(generations):
    for j, item in enumerate(generation):
        if item == ".":
            continue

        if item == "S" or item == "|":
            if len(generations) == i+1:
                # end of the line
                continue

            if generations[i+1][j] == "^":
                splits += 1
                generations[i+1][j-1] = "|"
                generations[i+1][j+1] = "|"
                continue

            generations[i+1][j] = "|"


print("total splits:", splits)
