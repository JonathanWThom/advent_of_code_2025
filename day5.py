ingredients = open("./day5_input.txt").read().split("\n\n")
fresh_ingredients = ingredients[0]
available_ingredients = ingredients[1].split("\n")[:-1]
fresh_ingredient_lines = fresh_ingredients.split("\n")
fresh_count = 0

for available in available_ingredients:
    for fresh_ingredient_line in fresh_ingredient_lines:
        ingredient_range = fresh_ingredient_line.split("-")
        lower = int(ingredient_range[0])
        upper = int(ingredient_range[1])
        if lower <= int(available) <= upper:
            fresh_count += 1
            break # Once it's been determined fresh, don't count it again

print(fresh_count)
