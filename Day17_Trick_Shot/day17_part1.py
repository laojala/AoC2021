y_target_range = [103, -58]

part1 = 0
for x in range(abs(y_target_range[0])):
    part1 += x

print(part1)
assert part1 == 5253
