import statistics

with open('day10.dat', 'r') as f:
    all_lines = [d.rstrip() for d in f.readlines()]

characters = {']': '[', ')': '(', '}': '{', '>': '<'}
illegals = []
incomplete_lines = []

for line in all_lines:
    blocks = []
    illegal = False
    for char in line:
        # loop characters and add ending characters to a list
        if char in characters.values():
            blocks.append(char)
        else:
            #if last character is a closing character
            if blocks[-1] == characters[char]:
                blocks.pop()
            else:
                illegals.append(char)
                illegal = True
                break
    if not illegal:
        incomplete_lines.append(blocks)

points_part1 = {')': 3, ']': 57, '}': 1197, '>': 25137}
part1 = 0

for illegal in illegals:
    part1 += points_part1[illegal]

print(part1)
assert part1 == 392139

points_part2 = {'(': 1, '[': 2, '{': 3, '<': 4}
scores_part2 = []

for line in incomplete_lines:
    line.reverse()
    score = 0
    for item in line:
        score = (score * 5) + points_part2[item]
    scores_part2.append(score)

part2 = statistics.median(scores_part2)
print(part2)
assert part2 == 4001832844




