
class TransparentOrigami:

    def __init__(self, layout):
        self.layout = layout
        # self.max_x = TransparentOrigami._max_x(self)
        # self.max_y = TransparentOrigami._max_y(self)

    # def _max_x(self):
    #     max_value = 0
    #     for x, y in self.layout:
    #         if x > max_value:
    #             max_value = x
    #     return max_value
    #
    # def _max_y(self):
    #     max_value = 0
    #     for x, y in self.layout:
    #         if y > max_value:
    #             max_value = y
    #     return max_value

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
print(part1)
