import statistics

# read input data
with open("day7.dat", 'r') as f:
    input = [d.split(",") for d in f.readlines()]

grabs = list(map(int, input[0]))

#part1
median = statistics.median(grabs)
part1 = 0
for grab in grabs:
    part1 = part1 + abs(grab - median)
print(part1)
#assert part1 == 328187


#part2
# triangular sequence
# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55
def triangular_distance(n):
    return int(n * (n + 1) / 2)


mean = int(statistics.mean(grabs))
print(statistics.mean(grabs))
print(mean)
part2 = 0

for grab in grabs:
    distance = abs(grab-mean)
    part2 = part2 + triangular_distance(distance)

print(part2)
#assert part2 == 91257582
