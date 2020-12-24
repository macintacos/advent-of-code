input = open("2020/src/input.txt", "r")
input_lines = sorted(input.readlines())

while len(input_lines) > 0:
    current_val = int(input_lines.pop(0))

    for val in input_lines:
        intified_val = int(val)
        if intified_val + current_val == 2020:
            print(intified_val, current_val)
            print(intified_val * current_val)

