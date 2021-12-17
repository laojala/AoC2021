class ShotSimulation:

    def __init__(self, velocity, target_x, target_y):
        self.position = [0, 0]
        self.velocity = velocity
        self.target_x = target_x
        self.target_y = target_y
        # assume that start position is never on target
        self.target_reached = False
        self.beyond_target = False

    def on_target(self):
        return self.target_reached

    def position(self):
        return self.position

    def step(self):
        x, y = self.position
        vel_x, vel_y = self.velocity

        new_pos = [x + vel_x, y + vel_y]

        if vel_x > 0:
            new_vel_x = vel_x - 1
        elif vel_x == 0:
            new_vel_x = vel_x
        else:  # vel_x < 0
            new_vel_x = vel_x + 1

        self.position = new_pos
        self.velocity = [new_vel_x, vel_y - 1]

    def is_on_target(self) -> bool:
        x, y = self.position
        x_low, x_high = self.target_x
        y_low, y_high = self.target_y

        if x in range(x_low, x_high + 1) and y in range(y_low, y_high + 1):
            return True
        return False

    def is_beyond_target(self) -> bool:
        x, y = self.position
        x_low, x_high = self.target_x
        y_low, y_high = self.target_y

        if x > x_high or y < y_low:
            return True
        return False

    def simulate_steps(self, steps=1000):
        """ Simulate steps until target reached or beyond target"""
        for step in range(steps):
            self.step()
            if self.is_on_target():
                self.target_reached = True
                break
            if self.is_beyond_target():
                self.beyond_target = True
                break


# # example
# x_target_range = [20, 30]
# y_target_range = [-10, -5]

# # # puzzle input
x_target_range = [265, 287]
y_target_range = [-103, -58]

part1 = 0
for x in range(abs(y_target_range[0])):
    part1 += x

print(f'part1: {part1}')
assert part1 == 5253


# part2: brute force, guessed the limits

on_target = []

for x in range(0, 289):
    for y in range(-104, 104):
        simulation = ShotSimulation([x, y], x_target_range, y_target_range)
        ShotSimulation.simulate_steps(simulation)
        if ShotSimulation.on_target(simulation):
            on_target.append([x, y])

part2 = len(on_target)
print(part2)
assert part2 == 1770
