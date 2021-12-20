with open("day20.data", 'r') as f:
    ALGORITHM = f.readline()


class TrenchMap:
    mask = [(-1, -1), (0, -1), (1, -1), (-1, 0), (0, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]

    def __init__(self, image):
        self.image = image
        self.space_pixel = "."

    def add_borders(self):
        # add 2 pixels of "space" to the beginning and end of a row
        for line in self.image:
            line.insert(0, self.space_pixel)
            line.insert(0, self.space_pixel)
            line.append(self.space_pixel)
            line.append(self.space_pixel)
        # then add 2 rows of space to the beginning and of the table
        dark_pixels = [self.space_pixel for i in range(0, len(self.image[0]))]
        self.image.insert(0, dark_pixels)
        self.image.insert(0, dark_pixels)
        self.image.append(dark_pixels)
        self.image.append(dark_pixels)

    def print_image(self):
        for line in self.image:
            print(line)

    def _get_pixel(self, y_ind, x_ind):
        number = ""
        for x, y in TrenchMap.mask:
            row = y_ind + y
            col = x_ind + x
            try:
                number = number + self.image[row][col]
            except IndexError:
                number = self.space_pixel

        return self._get_pixel_from_algorithm(number)

    @staticmethod
    def _get_pixel_from_algorithm(number: str):
        number = number.replace(".", "0")
        number = number.replace("#", "1")
        decimal = int(number, 2)
        return ALGORITHM[decimal]

    def enhance(self):
        self.add_borders()
        enhanced = []
        for index, line in enumerate(self.image):
            enhanced_row = []
            for x_index, pixel in enumerate(line):
                enhanced_row.append(self._get_pixel(index, x_index))
            enhanced.append(enhanced_row)
        self.image = enhanced
        # set new space pixel (that is 9 times space pixel)
        self.space_pixel = self._get_pixel_from_algorithm(self.space_pixel * 9)

    def loop_enhance(self, times):
        for index in range(times):
            self.enhance()

    def count_lights(self):
        return sum(item.count("#") for item in self.image)


with open("day20_image.data", 'r') as f:
    data = [list(d.rstrip()) for d in f.readlines()]


def get_results():
    image_part1 = TrenchMap(data[:])
    image_part1.loop_enhance(2)
    part1 = image_part1.count_lights()
    assert part1 == 5479

    # far from optimal, takes 6,5 seconds to run
    image_part2 = TrenchMap(data[:])
    image_part2.loop_enhance(50)
    part2 = image_part2.count_lights()
    assert part2 == 19012


get_results()
