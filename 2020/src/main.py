input = open("2020/src/input.txt", "r")
# input_lines = [1721, 979, 366, 299, 675, 1456]
input_lines = sorted(input.readlines())
previous_values = []

while len(input_lines) > 1:
    first_val = int(input_lines[0])
    previous_values.append(int(input_lines.pop(0)))

    for val in input_lines:
        intified_val = int(val)

        for prev_val in previous_values:
            if prev_val + intified_val + first_val == 2020:
                print(intified_val, prev_val, first_val)
                print(intified_val * prev_val * first_val)

