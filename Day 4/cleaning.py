f = open("input.txt", 'r')
input_text = f.read().splitlines()
f.close()

fully_overlapped_sections = 0
partially_overlapped_sections = 0

for pair in input_text:
    # Part 1
    sections = [sections.split('-') for sections in pair.split(',')]
    if (int(sections[0][0]) <= int(sections[1][0]) and int(sections[0][1]) >= int(sections[1][1])) or \
            (int(sections[1][0]) <= int(sections[0][0]) and int(sections[1][1]) >= int(sections[0][1])):
        fully_overlapped_sections += 1

    # Part 2
    sections = [list(range(int(s[0]), int(s[1])+1)) for s in sections]
    if len(set(sections[0]).intersection(set(sections[1]))) > 0:
        partially_overlapped_sections += 1

print("Number of fully overlapped sections:", fully_overlapped_sections)
print("Number of partially overlapped sections:", partially_overlapped_sections)
