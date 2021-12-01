import os


def read_report():
    file_path = (os.path.dirname(__file__)) + "/" + 'sonar_sweep.dat'

    with open(file_path) as f:
        input_data = [int(d) for d in f.readlines()]
    return input_data

def count_part1(sweep_data):
    counter = 0
    for i in range(1, len(sweep_data)):
        if sweep_data[i] > sweep_data[i - 1]:
            counter += 1
    return counter


def count_part2(sweep_data):
    sums = []
    for i in range( len(sweep_data)):
        if i > len(sweep_data) - 3:
            break
        sums.append(sweep_data[i] + sweep_data[i + 1] + sweep_data[i + 2])

    return count_part1(sums)


if __name__ == '__main__':
    data = read_report()

    part1_result = count_part1(data)
    print(part1_result)
    assert part1_result == 1184

    part2_result = count_part2(data)
    print(part2_result)
    assert part2_result == 1158
