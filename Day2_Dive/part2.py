import os

file_path = (os.path.dirname(__file__)) + "/" + "data.dat"

horizontal = 0
depth = 0
aim = 0

with open(file_path, "r") as f:
    for row in f.readlines():
        data = row.rstrip().split(" ")

        if (data[0]) == "forward":
            horizontal = horizontal + int(data[1])
            depth = depth + aim * int(data[1])

        if (data[0]) == "down":
            aim = aim + int(data[1])

        if (data[0]) == "up":
            aim = aim - int(data[1])


part2 = horizontal * depth
print(part2)
assert part2 == 2120734350


