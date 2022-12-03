f = open("input.txt", 'r')
input_text = f.read().splitlines()
f.close()

priorities = {chr(i): i % 96 for i in range(ord('a'), ord('z') + 1)}
priorities.update({chr(i): i % 64 + 26 for i in range(ord('A'), ord('Z') + 1)})
priorities_sum_part1 = 0

i = 0
group = list()
priorities_sum_part2 = 0

for items in input_text:
    i += 1

    # Part 1
    n = len(items)
    compartment1 = items[:n//2]
    compartment2 = items[n//2:]
    duplicate = (set(compartment1) & set(compartment2)).pop()
    priorities_sum_part1 += priorities[duplicate]

    # Part 2
    group.append(items)
    if i % 3 == 0:
        duplicate = (set(group[0]) & set(group[1]) & set(group[2])).pop()
        priorities_sum_part2 += priorities[duplicate]
        group.clear()

print("Sum of the priorities in Part 1:", priorities_sum_part1)
print("Sum of the priorities in Part 2:", priorities_sum_part2)
