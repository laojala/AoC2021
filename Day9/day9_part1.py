vents = []

f=open("day9.dat", "r")
for line in f:
    temp = line.strip('\n')
    temp = list(temp)
    temp = list(map(int, temp))
    vents.append(temp)
f.close()

low_points = []
list_low = []

max_x = len(vents)
max_y = len(vents[0])

# loop every point and count neigbours
for x in range(max_x):
    for y in range(max_y):
        point_value = vents[x][y]

        #upper value
        if x == 0:
            upper = 10 #higher than any number in the chart
        else:
            upper = vents[x-1][y]

        #right value
        if y == max_y-1:
            right = 10
        else:
            right = vents[x][y+1]

        # bottom value
        if x == max_x-1:
            bottom = 10
        else:
            bottom = vents[x+1][y]

        # left value
        if y == 0:
            left = 10
        else:
            left = vents[x][y-1]

        minimum = min(upper, right, bottom, left)
        if minimum > point_value:
            low_points.append(point_value)
            list_low.append((x,y))

part1 = len(low_points) + sum(low_points)
print("part1:", part1)
assert part1 == 560

# part2

basins = []

for point in list_low:
    not_crawled = []
    not_crawled.append(point)
    basin = []

    while not_crawled:
        point = not_crawled.pop(0)
        x = point[0]
        y = point[1]

        if point not in basin:
            basin.append(point)

        # upper point to not crawled if it is < 9
        if x != 0:
            temp = (x-1, y)
            if vents[x-1][y] < 9 and temp not in not_crawled and temp not in basin:
                not_crawled.append(temp)

        #right point
        if y != max_y-1:
            temp = (x, y+1)
            if vents[x][y+1] < 9 and temp not in not_crawled and temp not in basin:
                not_crawled.append(temp)

        # bottom point
        if x != max_x-1:
            temp = (x+1, y)
            if vents[x+1][y] < 9 and temp not in not_crawled and temp not in basin:
                not_crawled.append(temp)

        # left point
        if y != 0:
            temp = (x, y-1)
            if vents[x][y-1] < 9 and temp not in not_crawled and temp not in basin:
                not_crawled.append(temp)

    basins.append(basin)

# sort by length

lengths = list(map(lambda item: len(item), basins))
lengths = sorted(lengths, reverse=True)
part2 = lengths[0] * lengths[1] * lengths[2]
print("part2:", part2)
assert part2 == 959136



