from collections import defaultdict

def count_elements(number_of_rounds: int) -> int:

    # polymer = "NNCB"
    polymer = "CHBBKPHCPHPOKNSNCOVB"

    # create dictionary that contains number of elements
    elements_counter = defaultdict(int)
    # create dictionary that counts letters
    pairs = defaultdict(int)

    # init pairs from the initial polymer
    # also init counter for number of elements in the polymer
    for i, item in enumerate(polymer):
        element = polymer[i:i+2]
        elements_counter[item] += 1
        if len(element) == 1:
            continue
        pairs[element] += 1

    for rounds in range(number_of_rounds):
        next_pair = defaultdict(int)
        for pair in pairs:
            x, y = pair
            letter = rules[pair][:]
            new_pair1 = x + letter
            new_pair2 = letter + y
            next_pair[new_pair1] += pairs[pair]
            next_pair[new_pair2] += pairs[pair]
            # add new letter to the elements counter
            elements_counter[letter] += pairs[pair]
        pairs = next_pair.copy()

    return max(elements_counter.values()) - min(elements_counter.values())


with open("day14.dat", 'r') as f:
    all_lines = [d.rstrip() for d in f.readlines()]

rules = {}

for line in all_lines:
    a, b = line.split(" -> ")
    rules[a] = b

part1 = count_elements(10)
print(part1)
assert part1 == 3118

part2 = count_elements(40)
print(part2)
assert part2 == 4332887448171

