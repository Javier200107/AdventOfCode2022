f = open("input.txt", 'r')
input_text = f.readlines()
f.close()

current_calories = 0
calories_per_elf = list()
top_3_sum = 0

for calories in input_text:
    if calories.strip():
        current_calories += int(calories)
    else:
        calories_per_elf.append(current_calories)
        current_calories = 0

# Part 1
print("The Elf carrying the most is carrying", str(max(calories_per_elf)), "calories.")

# Part 2
calories_per_elf.sort(reverse=True)
print("Top 3 calories sum:", sum(calories_per_elf[:3]))
