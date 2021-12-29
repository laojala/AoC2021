
def read_data(file="day25.data"):
    with open(file) as f:
        input_data = [d.rstrip() for d in f.readlines()]

        return list(map(list, input_data))


cucumbers = read_data()
max_x = len(cucumbers[0])
max_y = len(cucumbers)

moves = True
steps_counter = 0

while moves:
    moves = False
    steps_counter += 1

    # move east
    for y, row in enumerate(cucumbers):
        new_row = [None] * max_x
        for x, char in enumerate(row):
            if char != ">":
                if not new_row[x]:
                    new_row[x] = char
                continue
            if x == max_x-1:
                if row[0] == "." and char == ">":
                    new_row[0] = char
                    new_row[x] = "."
                    moves = True
                else:
                    new_row[x] = char
                continue
            if row[x+1] == ".":
                new_row[x] = "."
                new_row[x+1] = char
                moves = True
            else:
                new_row[x] = char

        cucumbers[y] = new_row[:]
    new_cucumbers = [[] for i in range(max_y)]
    for item in new_cucumbers:
        for x in range(max_x):
            item.append([])

    # moving south
    for y, row in enumerate(cucumbers):
        for x, char in enumerate(row):
            if char != "v":
                if not new_cucumbers[y][x]:
                    new_cucumbers[y][x] = char
                continue
            if y == max_y-1:
                if cucumbers[0][x] == ".":
                    new_cucumbers[0][x] = char
                    new_cucumbers[y][x] = "."
                    moves = True
                else:
                    new_cucumbers[y][x] = char
                continue
            if cucumbers[y+1][x] == ".":
                new_cucumbers[y+1][x] = char
                new_cucumbers[y][x] = "."
                moves = True
                continue
            else:
                new_cucumbers[y][x] = char

    cucumbers.clear()
    cucumbers = new_cucumbers[:]

print("steps:", steps_counter)
assert 534 == steps_counter
