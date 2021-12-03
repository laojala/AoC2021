import os

file_path = (os.path.dirname(__file__)) + "/" + "data.dat"

with open(file_path, "r") as f:
    input_data = [d.rstrip() for d in f.readlines()]

length = len(input_data[0]) - 1

counter = [0] * (length + 1)

for index in range(length):
    for value in input_data:
        if value[index] == "1":
            counter[index] += 1

gamma = ""
epsilon = ""

for value in counter:
    if value >= len(input_data)/2:
        gamma += "1"
        epsilon += "0"
    else:
        gamma += "0"
        epsilon += "1"

part1 = int(gamma, 2) * int(epsilon,2)

print(part1)

assert part1 == 2640986