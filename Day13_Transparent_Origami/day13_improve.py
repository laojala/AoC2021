
class TransparentOrigami:

    def __init__(self, layout):
        self.layout = layout

    def print(self):
        max_x = max(c[0] for c in self.layout)
        max_y = max(c[1] for c in self.layout)
        for row in range(max_y+1):
            print_line = ""
            for col in range(max_x+1):
                if [row, col] in self.layout:
                    print_line = print_line + "#"
                else:
                    print_line = print_line + " "
            print(print_line)

    def dots(self):
        return len(self.layout)

    def fold_up_y(self, y_axe):
        temp_layout = self.layout[:]
        for item in temp_layout:
            x, y = item
            if y < y_axe:
                continue
            self.layout.remove([x, y])
            new_dot = [x, abs(y - (2 * y_axe))]
            if new_dot not in self.layout:
                self.layout.append(new_dot)

    def fold_left_x(self, x_axe):
        temp_layout = self.layout[:]
        for item in temp_layout:
            x, y = item
            if x < x_axe:
                continue
            self.layout.remove([x, y])
            new_dot = [abs(x-(2*x_axe)), y]
            if new_dot not in self.layout:
                self.layout.append(new_dot)

    def __repr__(self):
        return f"{self.layout}"


with open("day13.dat", 'r') as f:
    temp = [d.rstrip().split(",") for d in f.readlines()]
    all_lines = []
    for line in temp:
        temp = list(map(int, line))
        all_lines.append(temp)

paper = TransparentOrigami(all_lines)
paper.fold_left_x(655)
part1 = paper.dots()
assert part1 == 837
paper.fold_up_y(447)

paper.fold_left_x(327)
paper.fold_up_y(223)

paper.fold_left_x(163)
paper.fold_up_y(111)

paper.fold_left_x(81)
paper.fold_up_y(55)

paper.fold_left_x(40)
paper.fold_up_y(27)

paper.fold_left_x(13)
paper.fold_up_y(6)

paper.print()
