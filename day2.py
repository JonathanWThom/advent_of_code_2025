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
    if length % 2 != 0:
        return False

    half = int(length / 2)

    # print(str(i))
    # print(str(i)[half:])
    # print(str(i)[:half])
    return str(i)[half:] == str(i)[:half]

counter = 0
ranges = open("./day2_input.txt").read().replace("\n", "").split(",")
# some of these can be ruled out earlier if they only contain odd lengths
for rang in ranges:
    start_and_finish = rang.split("-")
    start = int(start_and_finish[0])
    finish = int(start_and_finish[1])
    for i in range(start, finish+1):
        if is_invalid(i):
            counter += i


print(counter)
