# create dictionary for days and number of fish on that day
initial_fish = dict.fromkeys([0, 1, 2, 3, 4, 5, 6, 7, 8], 0)

# read input data
with open("day6.dat", 'r') as f:
    input = [d.split(",") for d in f.readlines()]

# map input data to integers
list_of_all_fish = list(map(int, input[0]))

# add number of fish to a dictionary
fish = initial_fish.copy()

for item in list_of_all_fish:
    fish[item] += 1

# process days

def count_fish(days, fish, initial_fish):

    for day in range(days):

        next_day = initial_fish.copy()

        for item in fish:
            if item == 0:
                next_day[8] = fish[0]
                next_day[6] = fish[0]
                continue

            if item == 7:
                next_day[6] = next_day[6] + fish[7]
                continue

            next_day[item-1] = fish[item]

        fish = next_day.copy()

    return(sum(fish.values()))

part1 = count_fish(80, fish, initial_fish)
part2 = count_fish(256, fish, initial_fish)
print(part1)
print(part2)

assert part1 == 365862
assert part2 == 1653250886439

