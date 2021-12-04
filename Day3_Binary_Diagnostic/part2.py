import os
import numpy as np


def transpose_matrix(matrix):
    temp = np.transpose(matrix)
    return np.array(temp).tolist()

file_path = (os.path.dirname(__file__)) + "/" + "data.dat"

with open(file_path, "r") as f:
    input_data = [list(d.rstrip()) for d in f.readlines()]

oxygen = input_data[:]

for index in range(len(input_data[0])):
    if len(oxygen) == 1:
        break

    transposed = []
    transposed = transpose_matrix(oxygen[:])
    ones = transposed[index].count('1')
    zeros = transposed[index].count('0')

    if ones >= zeros:
        more = '1'
    else:
        more = '0'

    for index_2, item in enumerate(oxygen):
        if item[index] != more:
            oxygen[index_2] = "REMOVE"

    while "REMOVE" in oxygen: oxygen.remove("REMOVE")



ox = "".join(oxygen[0])
print(int(ox, 2))

scrubber = input_data[:]

for index in range(len(input_data[0])):
    if len(scrubber) == 1:
        break

    transposed = []
    transposed = transpose_matrix(scrubber[:])
    ones = transposed[index].count('1')
    zeros = transposed[index].count('0')

    if ones >= zeros:
        more = '1'
    else:
        more = '0'

    for index_2, item in enumerate(scrubber):
        if item[index] == more:
            scrubber[index_2] = "REMOVE"

    while "REMOVE" in scrubber: scrubber.remove("REMOVE")

sc = "".join(scrubber[0])
print(int(sc, 2))

print(int(ox, 2) * int(sc, 2))

assert int(ox, 2) * int(sc, 2) == 6822109