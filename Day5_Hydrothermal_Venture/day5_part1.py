# Algorithm from https://github.com/lizthegrey/adventofcode/blob/main/2021/day05.go
# https://youtu.be/A5ZmYSr1mlw


def add_point(point):
    if point in coordinates:
        coordinates[point] += 1
    else:
        coordinates[point] = 1


# tuple of coordinate as a key
coordinates = {}

# read input data

with open("day5.dat", 'r') as f:
    all_lines = [d.rstrip() for d in f.readlines()]

# process lines in input_data

for line in all_lines:
    temp = line.split(" -> ")

    startX = int(temp[0].split(",")[0])
    startY = int(temp[0].split(",")[1])
    endX = int((temp[1].split(","))[0])
    endY = int((temp[1].split(","))[1])

    if startX == endX:
        if startY < endY:
            for index in range(startY, endY+1):
                add_point((startX, index))
        else:
            for index in range(startY, endY-1, -1):
                add_point((startX, index))
    elif startY == endY:
        if startX < endX:
            for index in range(startX, endX+1):
                add_point((index, startY))
        else:
            for index in range(startX, endX-1, -1):
                add_point((index, startY))
    # else:
        # part1 not handling lines that are not horizontal or vertical


count = 0
for item in coordinates:
    if coordinates[item] >= 2:
        count += 1

print(count)
assert count == 7380

