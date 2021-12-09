vents = []

f=open("day9.dat", "r")
for line in f:
    temp = line.strip('\n')
    temp = list(temp)
    temp = list(map(int, temp))
    vents.append(temp)
f.close()

low_points = []

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

part1 = len(low_points) + sum(low_points)
print(part1)
#assert part1 == 560
