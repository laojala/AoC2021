import numpy as np

def bingo(table, called):
    sum_of_not_called = 0
    for line in table:
        for item in line:
            if item not in called:
                sum_of_not_called = sum_of_not_called + item
    print("BINGO:", table)
    print("last called", called[-1])
    print("sum", sum_of_not_called)
    part2 = sum_of_not_called * called[-1]
    print(part2)
    assert part2 == 12635
    exit()


#def _readGroup(filename='bingo_example.dat'):
def _readGroup(filename='bingo.dat'):

    with open(filename, 'r') as f:
        all_lines = f.readlines()

    entry = []
    data = []

    for index, line in enumerate(all_lines):
        if line != '\n':
            temp = line.rstrip()
            entry.append(list(map(int, temp.split())))
        if line == '\n' or index == len(all_lines) - 1:
            data.append(entry)
            entry = []

    return data


with open("call.dat", "r") as f:
#with open("call_example.dat", "r") as f:
    input_data = [d.split(",") for d in f.readlines()]
call = list(map(int, input_data[0]))

called = call[:4]
not_called = call[4:]

boards = _readGroup()

for i in range(len(call) - 4):

    called.append(not_called.pop(0))

    # if there are only one board left, call BINGO!
    if boards.count("BINGO") == len(boards) - 1:
        boards = list(filter(lambda x: x != "BINGO", boards))
        bingo(boards[0], called)

    for index, board in enumerate(boards):

        if board == "BINGO":
            continue

        temp_board = board[:]
        temp_transposed = np.transpose(board).tolist()
        temp_board = temp_board + temp_transposed
        for line in temp_board:
            count_called = 0
            for number in called:
                if number in line:
                    count_called += 1
                    if count_called == 5:
                        boards[index] = "BINGO"
                        # Bingo(board, called)
