# start counter at 0
# get ranges by splitting on comma
# for each range, split on "-"
# first value is start, last value is end
# loop
# for each value, assess if it's invalid
# if its length is odd, it's not invalid and can be skipped
# otherwise, take its length and divide by two
# slice off the first n chars and compare to the last n chars
# if they are equal, then add it to the counter
# return counter

def is_invalid(i):
    length = len(str(i))
    if int_is_odd(i):
        return False

    half = int(length / 2)

    return str(i)[half:] == str(i)[:half]

def int_is_odd(i):
    return len(str(i)) % 2 != 0

counter = 0
ranges = open("./day2_input.txt").read().replace("\n", "").split(",")
for rang in ranges:
    start_and_finish = rang.split("-")
    start = int(start_and_finish[0])
    finish = int(start_and_finish[1])
    if int_is_odd(start) & int_is_odd(finish):
        next

    for i in range(start, finish+1):
        if is_invalid(i):
            counter += i


print(counter)
