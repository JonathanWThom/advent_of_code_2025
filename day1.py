zero_counter = 0
location = 50

# read file
instructions = open("./day1_input.txt").read().split("\n")
for instruction in instructions:
    if instruction:
        direction = instruction[0]
        magnitude = int(instruction[1:])
        # need to account for multiple rotations.
        if magnitude > 100:
            magnitude = magnitude % 100

        if direction == "L":
            magnitude = magnitude * -1

        location = location + magnitude
        if location < 0:
            location = 100 + location
        elif location > 99:
            location = location - 100

        if location == 0:
            zero_counter += 1

# for each line in file, split into direction and how_many
# if right, we are going positive
# if left, we are going negative
# apply instruction
# if value is less than zero, subtract that many from 100 (or 99?)
# if value is greater than 99, add that many to 0 (-1?)
# get current location
# if location is zero, increment counter

print(zero_counter)
