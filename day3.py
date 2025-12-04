total_joltage = 0
banks = open("./day3_input.txt").read().split("\n")[:-1]

for bank in banks:
    max_value = max(bank[:-1])
    max_value_indices = [i for i, x in enumerate(bank[:-1]) if x == max_value]

    best_new_joltage = 0
    for i in max_value_indices:
        available = bank[i+1:]
        new_joltage = int(bank[i] + max(available))
        if new_joltage > best_new_joltage:
            best_new_joltage = new_joltage

    joltage = best_new_joltage

    total_joltage += joltage

print("total joltage:", total_joltage)
