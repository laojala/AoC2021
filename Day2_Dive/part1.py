import os

file_path = (os.path.dirname(__file__)) + "/" + "data.dat"

horizontal = 0
depth = 0

with open(file_path, "r") as f:
    for row in f.readlines():
        data = row.rstrip().split(" ")

        if (data[0]) == "forward":
            horizontal = horizontal + int(data[1])

        if (data[0]) == "down":
            depth = depth + int(data[1])

        if (data[0]) == "up":
            depth = depth - int(data[1])


part1 = horizontal * depth
print(part1)

assert part1 == 1893605
