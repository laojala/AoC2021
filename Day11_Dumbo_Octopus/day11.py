class OctopusCave:
    NEIGHBOURS = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]

    def __init__(self, octopus_layout):
        self.layout = octopus_layout
        self.flash_history = 0
        self.rows = len(octopus_layout)
        self.columns = len(octopus_layout[0])

    def add_flash(self, flashes=1):
        self.flash_history += flashes

    def __repr__(self):
        return f"Flashes: {self.flash_history}\nData: \n {self.layout}."

    def print_lines(self):
        for line in self.layout:
            print(line)

    def print_flash_history(self):
        print(self.flash_history)

    def add_one_to_each(self):
        for line in self.layout:
            for index, item in enumerate(line):
                line[index][0] = item[0] + 1

    def loop_flashes(self):

        # loop while there are values that have not flashed

        while True:
            # stop if there are no [>9, 0] in the octopus cave

            flashes_left = False

            for line in self.layout:
                if flashes_left:
                    break
                for item in line:
                    if item[0] > 9 and item[1] == 0:
                        flashes_left = True
                        break

            if not flashes_left:
                return

            for line_index, line in enumerate(self.layout):
                for column_index, item in enumerate(line):
                    # do nothing if already flashed
                    value = self.layout[line_index][column_index][0]
                    flash_value = self.layout[line_index][column_index][1]
                    # has flashed
                    if flash_value == 1:
                        continue
                    # if value is 9 but is not flashed:
                    elif value > 9 and flash_value == 0:
                        # set flash value to 1
                        self.layout[line_index][column_index][1] = 1
                        # add a new flash
                        self.add_flash()
                        # set new values for neighbours:
                        for x, y in self.NEIGHBOURS:
                            col = column_index + x
                            row = line_index + y
                            if 0 <= col < self.columns and 0 <= row < self.rows:
                                if self.layout[row][col][1] == 0:
                                    self.layout[row][col][0] = self.layout[row][col][0] + 1

    def set_flashes_to_0(self):
        number_of_flashes = 0
        for index, line in enumerate(self.layout):
            for i, item in enumerate(line):
                if item[0] >= 9 and item[1] != 0:
                    self.layout[index][i] = [0, 0]
                    number_of_flashes += 1

        return number_of_flashes

    def loop_cave(self, rounds: int, loop_until_all_flash=False) -> None:
        for i in range(rounds):
            self.add_one_to_each()  # add one to each item
            self.loop_flashes()
            number = self.set_flashes_to_0()

            if loop_until_all_flash and number == 100:
                print(f"Breaking execution, all flashing at round, {i+1}")
                break


def _read_input(file="day11.dat"):
    data = []

    with open(file, 'r') as f:
        data = [list(d.rstrip()) for d in f.readlines()]
        # loop items of a line and move them to int
        # first time that I use list comprehension nested :-)
        data = [[[int(item), 0] for item in line] for line in data]
        return data

if __name__ == "__main__":
    layout = OctopusCave(_read_input())
    layout.loop_cave(100)
    layout.print_flash_history()
    #1700

    # part 2: print
    layout2 = OctopusCave(_read_input())
    layout2.loop_cave(1000, True)
    #273
