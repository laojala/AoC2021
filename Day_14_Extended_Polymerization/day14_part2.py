from functools import reduce
from itertools import chain
from collections import defaultdict

with open("day14.dat", 'r') as f:
    all_lines = [d.rstrip() for d in f.readlines()]

rules = {}

for line in all_lines:
    a, b = line.split(" -> ")
    rules[a] = b

#polymer = "NNCB"
polymer = "CHBBKPHCPHPOKNSNCOVB"

unique_keys = list(chain.from_iterable(rules.keys()))
unique_values = list(rules.values())
unique = set(chain(unique_keys, unique_values))

elements_counter = {}
for item in unique:
    elements_counter[item] = 0

# create dictionary that counts letters
pairs = defaultdict(int)

# init polymer keys for the first round
# also init counter for number of letters in the polymer
for i, item in enumerate(polymer):
    element = polymer[i:i+2]
    elements_counter[item] += 1
    if len(element) == 1:
        continue
    pairs[element] += 1

next_pair = {}

for rounds in range(40):
    next_pair.clear()
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
    pairs.clear()
    pairs = next_pair.copy()


print(elements_counter)

part2 = max(elements_counter.values()) - min(elements_counter.values())
print(part2)
assert part2 == 4332887448171

