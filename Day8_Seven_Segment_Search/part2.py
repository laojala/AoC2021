with open("day8_example.dat", 'r') as f:
    all_lines = [d.rstrip() for d in f.readlines()]

inputs = []
outputs = []

for line in all_lines:
    temp = line.split(" | ")
    temp_input = temp[0].split()
    temp_output = temp[1].split()
    input_sorted = map(lambda x: "".join(sorted(x)), temp_input)
    output_sorted = map(lambda x: "".join(sorted(x)), temp_output)
    inputs.append(list(input_sorted))
    outputs.append(list(output_sorted))

print(inputs)
print(outputs)

# process mapping to letters
# positions (a is index 0, b is index 1 etc):

#  aaaa
# b    c
# b    c
#  dddd
# e    f
# e    f
#  gggg

output_sum = 0

for index, input in enumerate(inputs):
    digits = {}
    map_later = []

    positions = {}

    for item in input:
        if len(item) == 2:
            digits[1] = item
            continue
        if len(item) == 4:
            digits[4] = item
            continue
        if len(item) == 3:
            digits[7] = item
            continue
        if len(item) == 7:
            digits[8] = item
            continue
        map_later.append(item)

    # digit that is not in 1 but is in 7 is upper horizontal line (position "a")
    for digit in digits[7]:
        if digit not in digits[1]:
            positions["a"] = digit

    pop_later = []
    print(digits)
    print(positions)

    print("ALL MAP LATER:", map_later)

    # determine number 3 and 6
    for i in range(len(map_later)-1):
        print("******************")
        # either 3,2,5
        print("map later:", map_later[i])
        print("digits[1]:", digits[1])
        print("LEN:", len(map_later[i]))
        print(digits[1][0] in map_later[i] and digit[1][1] in map_later[i])
        print("NOT", digits[1][0] not in map_later[i] or digits[1][1] not in map_later[i])
        print(digits)
        if len(map_later[i]) == 5:
            if digits[1][0] in map_later[i] or digit[1][1] in map_later[i]:
                digits[3] = map_later[i]
                print("5 HEREEE")
                # remove "3" from map_later
                pop_later.append(i)
        # either 0, 6, 9
        if len(map_later[i]) == 6:
            if digits[1][0] not in map_later[i] or digits[1][1] not in map_later[i]:
                print("6 HEREEE")
                digits[6] = map_later[i]
                pop_later.append(i)

    print("END:", digits)
    pop_later.sort(reverse=True)

    for i in pop_later:
        map_later.pop(i)

    # we know 1, 3, 4, 6, 7, 8 and index a
    # we don't know 2,5
    # we don't know 0,9

    # determine e, so we can distinguish rest of the missing numbers

    # first, determine c, it is missing from 6 compared to 8. And determine f using 1:
    for digit in digits[8]:
        if digit not in digits[6]:
            positions["c"] = digit
            # determine also f as we know 1 and "c"
            for letter in digits[1]:
                if letter != digit:
                    positions["f"] = letter
            break

    # we know a, c, f
    # compare 3 and 4 and determine d:
    temp3 = digits[3]

    for digit in digits[3]:
        if digit in digits[4] or digit == positions["a"]:
            temp3 = temp3.replace(digit, "")

    positions["g"] = temp3

    for digit in digits[3]:
        if digit not in positions.values():
            positions["d"] = digit

    #  aaaa
    # b    c
    # b    c
    #  dddd
    # e    f
    # e    f
    #  gggg

    # we have enough information to calculate more positions
    # we don't know 2,5
    # we don't know 0,9
    # we positions a,c,d,f,g

    for item in map_later:
        if len(item) == 5 and positions["f"] in item:
            digits[5] = item
        if len(item) == 5 and positions["f"] not in item:
            digits[2] = item
        if len(item) == 6 and positions["d"] in item:
            digits[9] = item
        if len(item) == 6 and positions["d"] not in item:
            digits[0] = item

    reversed = my_dict = {digits[k]:k for k in digits}
    print(reversed)
    print(len(reversed))
    print(positions)
    output_temp = ""
    for output in outputs[index]:
        output_temp = output_temp + str(reversed[output])
#bcdef
    output_sum = output_sum + int(output_temp)

print(output_sum)