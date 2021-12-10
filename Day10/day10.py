
with open('day10.dat', 'r') as f:
    all_lines = [d.rstrip() for d in f.readlines()]

characters = {']': '[', ')': '(', '}': '{', '>': '<'}
illegals = []

for line in all_lines:
    blocks = []
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
                break


points = {')': 3, ']': 57, '}': 1197, '>': 25137}
part1 = 0

for illegal in illegals:
    part1 += points[illegal]

print(part1)
assert part1 == 392139



