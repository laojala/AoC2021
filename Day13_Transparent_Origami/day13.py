
class TransparentOrigami:

    def __init__(self, layout):
        self.layout = layout

    def print(self):
        print("**********PAPER************")
        max_y = max(c[0] for c in self.layout)
        max_x = max(c[1] for c in self.layout)
        for row in range(max_x+1):
            print_line = ""
            for col in range(max_y+1):
                if (col, row) in self.layout:
                    print_line = print_line + "#"
                else:
                    print_line = print_line + "."
            print(print_line)

    def dots(self):
        return len(self.layout)

    def fold_y(self, y_axe):
        temp_layout = self.layout[:]
        for item in temp_layout:
            x, y = item
            if y < y_axe:
                continue
            self.layout.remove((x, y))
            new_dot = (x, abs(2 * y_axe - y))
            if new_dot not in self.layout:
                self.layout.append(new_dot)

    def fold_x(self, x_axe):
        temp_layout = self.layout[:]
        for item in temp_layout:
            x, y = item
            if x < x_axe:
                continue
            self.layout.remove((x, y))
            new_dot = (abs(2*x_axe - x), y)
            if new_dot not in self.layout:
                self.layout.append(new_dot)

    def __repr__(self):
        return f"{self.layout}"


with open("day13_example.dat", 'r') as f:
    temp = [d.rstrip().split(",") for d in f.readlines()]
    all_lines = []
    for line in temp:
        temp = tuple(map(int, line))
        all_lines.append(temp)


paper = TransparentOrigami(all_lines)
print(paper)
paper.print()

paper.fold_y(7)
paper.print()
paper.fold_x(5)
paper.print()
# # #
# paper.fold_x(655)
# part1 = paper.dots()
# print(part1)
# assert part1 == 837
#
# paper.fold_y(447)
#
# paper.fold_x(327)
# paper.fold_y(223)
#
# paper.fold_x(163)
# paper.fold_y(111)
#
# paper.fold_x(81)
# paper.fold_y(55)
#
# paper.fold_x(40)
# paper.fold_y(27)
#
# paper.fold_x(13)
# paper.fold_y(6)
# paper.print()


# fold along x=655
# fold along y=447
# fold along x=327
# fold along y=223
# fold along x=163
# fold along y=111
# fold along x=81
# fold along y=55
# fold along x=40
# fold along y=27
# fold along y=13
# fold along y=6
