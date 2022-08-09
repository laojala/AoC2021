from collections import defaultdict


def read_data(file="day25_example.data"):
    with open(file) as f:
        input_data = [d.rstrip() for d in f.readlines()]

        data = defaultdict(lambda: defaultdict(dict))

        max_row = 0

        for y, line in enumerate(input_data):
            data[y] = {}
            for x, item in enumerate(line):
                if x > max_row:
                    max_row = x
                if item == ".":
                    continue
                elif item == ">":
                    data[y][x] = ">"
                else:
                    data[y][x] = "v"

        return max_row, data


x_max, cucumbers = read_data()
y_max = max(cucumbers.keys())

print(cucumbers)

# print("max y", y_max) # 136
# print("max x", x_max) # 138

moves = True
steps_counter = 0

while moves:
    moves = False
    steps_counter += 1

    # take step east
    for item in range(0, y_max):
        new_value_for_key = defaultdict()
        for pos in cucumbers[item]:
            character = cucumbers[item][pos]
            if character != ">":
                new_value_for_key[pos] = character
                continue
            if pos == x_max:
                if 0 not in cucumbers[item].keys():
                    new_value_for_key[0] = character
                    moves = True
                else:
                    new_value_for_key[pos] = character
                continue
            if pos + 1 not in cucumbers[item].keys():
                new_value_for_key[pos + 1] = character
                moves = True
            else:
                new_value_for_key[pos] = character
        cucumbers[item] = new_value_for_key

    new_cucumbers = defaultdict(lambda: defaultdict(dict))

    # take step south. loop row by row
    for key in range(y_max):
        for pos in cucumbers[key]:
            character = cucumbers[key][pos]
            if character != "v":
                new_cucumbers[key][pos] = character
                continue
            # handle last row differently
            if key == y_max:
                if pos not in cucumbers[0].keys():
                    new_cucumbers[0][pos] = character
                    moves = True
                else:
                    new_cucumbers[key][pos] = character
                continue
            if pos not in cucumbers[key + 1].keys():
                new_cucumbers[key + 1][pos] = character
                moves = True
            else:
                new_cucumbers[key][pos] = character
        cucumbers = new_cucumbers[:]
        # print(steps_counter)

    moves = False

print(steps_counter)
print(cucumbers)
