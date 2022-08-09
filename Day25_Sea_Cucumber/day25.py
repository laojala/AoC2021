def read_data(file="day25.data"):
    with open(file) as f:
        input_data = [d.rstrip() for d in f.readlines()]

        cucumbers = {">": [], "v": []}

        for y, line in enumerate(input_data):
            for x, item in enumerate(line):
                if item == ".":
                    continue
                elif item == ">":
                    cucumbers[">"].append((x, y))
                else:
                    cucumbers["v"].append((x, y))

        return cucumbers, len(input_data[0])-1, len(input_data)-1


def new_postion(pos, max_pos):
    if pos + 1 > max_pos:
        return 0
    else:
        return pos + 1


sea_bottom, x_max, y_max = read_data()

moves = True
steps_counter = 0

#for i in range(1):
while moves:
    moves = False
    steps_counter += 1
    # take step east
    new_east = []
    for sea_cucumber in sea_bottom[">"]:
        old_pos = sea_cucumber[0], sea_cucumber[1]
        # count new positions
        next_pos = new_postion(old_pos[0], x_max), old_pos[1]
        # take step if position is not occupied
        if next_pos not in sea_bottom["v"] and next_pos not in sea_bottom[">"]:
            new_east.append(next_pos)
            moves = True
        else:
            new_east.append(old_pos)


    sea_bottom[">"] = new_east[:]

    new_south = []

    # take step south
    for sea_cucumber in sea_bottom["v"]:
        old_pos = sea_cucumber[0], sea_cucumber[1]
        # count new positions
        next_pos = (old_pos[0], new_postion(old_pos[1], y_max))
        # take step if position is not occupied
        if next_pos not in sea_bottom["v"] and next_pos not in sea_bottom[">"]:
            new_south.append(next_pos)
            moves = True
        else:
            new_south.append(old_pos)

    sea_bottom["v"] = new_south[:]
    print(steps_counter)
print(steps_counter)

# 534 is the right answer - algorithm takes as many seconds to run...