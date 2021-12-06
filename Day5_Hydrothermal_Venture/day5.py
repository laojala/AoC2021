# Algorithm in courtesy of Liz Fong-Jones

# https://youtu.be/A5ZmYSr1mlw
# https://github.com/lizthegrey/adventofcode/blob/main/2021/day05.go

def add_point(point, coordinates):
    if point in coordinates:
        coordinates[point] += 1
    else:
        coordinates[point] = 1


# tuple of coordinate as a key
part1 = {}
part2 = {}

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
                add_point((startX, index), part1)
                add_point((startX, index), part2)
        else:
            for index in range(startY, endY-1, -1):
                add_point((startX, index), part1)
                add_point((startX, index), part2)
    elif startY == endY:
        if startX < endX:
            for index in range(startX, endX+1):
                add_point((index, startY), part1)
                add_point((index, startY), part2)
        else:
            for index in range(startX, endX-1, -1):
                add_point((index, startY), part1)
                add_point((index, startY), part2)
    else:
        if startX < endX:
            yIncr = 1
            if startY > endY:
                yIncr = -1
            y = startY
            for x in range(startX, endX+1):
                add_point((x, y), part2)
                y += yIncr
        else:
            yIncr = 1
            if startY > endY:
                yIncr = -1
            y = startY
            for x in range(startX, endX-1, -1):
                add_point((x, y), part2)
                y += yIncr



count1 = 0
count2 = 0

for item in part1:
    if part1[item] >= 2:
        count1 += 1

for item in part2:
    if part2[item] >= 2:
        count2 += 1

print(count1)
assert count1 == 7380

print(count2)
assert count2 == 21373
