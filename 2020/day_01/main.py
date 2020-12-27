input = open("./input.txt", "r")
input_lines = sorted(input.readlines())
previous_values = []

while len(input_lines) > 1:
    first_val = int(input_lines[0])
    previous_values.append(int(input_lines.pop(0)))

    for val in input_lines:
        intified_val = int(val)

        for prev_val in previous_values:
            if prev_val + intified_val + first_val == 2020:
                print(f"Values found: {intified_val, prev_val, first_val}")
                print(f"Computed value: {intified_val * prev_val * first_val}")

