with open("day8.dat", 'r') as f:
    all_lines = [d.rstrip() for d in f.readlines()]

outputs = []

for line in all_lines:
    temp = line.split(" | ")
    outputs.append(temp[1].split())


part1 = 0
known = [2, 3, 4, 7]

for output in outputs:
    for item in output:
        length = len(item)
        if length in known:
            part1 += 1

print(part1)
assert part1 == 452