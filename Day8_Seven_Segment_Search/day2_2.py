with open("day8.dat", 'r') as f:
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

output_sum = 0

for index, input in enumerate(inputs):
    digits = {}
    map_later = []

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

    assert len(map_later) == 6

    for item in map_later:

        segments = set(item)

        if len(item) == 5:
            if len(segments.intersection(set(digits[1]))) == 2 and len(item) == 5:
                digits[3] = item
            elif len(segments.intersection(set(digits[4]))) == 2 and len(item) == 5:
                digits[2] = item
            else:
                digits[5] = item

        if len(item) == 6:
            if set(digits[4]).issubset(segments) and len(item) == 6:
                digits[9] = item
            elif not set(digits[1]).issubset(segments) and len(item) == 6:
                digits[6] = item
            else:
                digits[0] = item

    reversed = {digits[k]: k for k in digits}
    output_temp = ""
    for output in outputs[index]:
        output_temp = output_temp + str(reversed[output])
    output_sum = output_sum + int(output_temp)

print(output_sum)
assert output_sum == 1096964