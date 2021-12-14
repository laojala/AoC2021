#not optimal algorithm, can't solve part2

with open("day14.dat", 'r') as f:
    all_lines = [d.rstrip() for d in f.readlines()]

rules = {}

for line in all_lines:
    a, b = line.split(" -> ")
    rules[a] = b

#polymer = "NNCB"
polymer = "CHBBKPHCPHPOKNSNCOVB"

for rounds in range(10):

    new_polymer = polymer[0]

    for i, letter in enumerate(polymer):
        element = polymer[i:i+2]

        if len(element) == 1:
            continue
        new_polymer = new_polymer + rules[element] + polymer[i+1]
    polymer = new_polymer

unique = set(polymer)
letters = {}

for letter in unique:
    count = polymer.count(letter)
    letters[letter] = count

part1 = max(letters.values()) - min(letters.values())

print(part1)
assert part1 == 3118