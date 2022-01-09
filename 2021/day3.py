"""Day 3."""


from typing import Counter


def puzzle_input(is_test=False) -> list[str]:
    """Gets the puzzle input."""
    if is_test:
        return [
            "00100",
            "11110",
            "10110",
            "10111",
            "10101",
            "01111",
            "00111",
            "11100",
            "10000",
            "11001",
            "00010",
            "01010",
        ]

    input: list[str] = []
    with open("./day_3.txt", "r") as file:
        for line in file:
            input.append(line)

    return input


def transpose_strings(binaries: list[str], pos: int) -> list[str]:
    """Gets a list of strings and returns a transposed version of it."""
    transposed_strings: list[str] = []

    new_binary: str = ""
    for j in range(len(binaries)):
        if binaries[j][pos] == "\n":
            continue  # skip the newline in the input
        new_binary += binaries[j][pos]

    if new_binary != "":
        transposed_strings.append(new_binary)

    return transposed_strings


def get_rating(input: list[str], rating_type: str) -> str:  # noqa
    rating = ""
    print(f"{ len(input) = }")

    for pos in range(len(input)):
        print(f"--- NEW ITERATION FOR: {rating_type} ---")
        if len(input) == 2:
            print(f"{sorted(input) = }")
            rating = sorted(input)[-1] if rating_type == "oxygen" else sorted(input)[0]
            break
        else:
            print(f"{pos = }")
            current_bit = transpose_strings(input, pos)
            print(f"{current_bit = }")
            counter = Counter(current_bit[0]).most_common()
            print(f"{counter = }")

            if counter[0][1] == counter[1][1]:
                significant_bit = "1" if rating_type == "oxygen" else "0"
            else:
                significant_bit = (
                    counter[0][0] if rating_type == "oxygen" else counter[1][0]
                )
            print(f"{significant_bit = }, {pos = }")
            print(f"Starting with: {input = }")

            new_input = []
            for idx, val in enumerate(input):
                print(f"{idx = }, {val = }")
                if val[pos] == significant_bit:
                    print(
                        f"Found '{val}', going to keep because "
                        f"position '{pos}' matches '{significant_bit}'"
                    )
                    new_input.append(input[idx])

            input = new_input

        print(f"{input = }")
        if len(input) == 1:
            break

    print()
    return rating


def main() -> None:
    """Does the main things."""
    input: list[str] = puzzle_input(is_test=False)

    oxygen_gen_rating: str = get_rating(input.copy(), "oxygen")
    co2_scrubber_rating: str = get_rating(input.copy(), "co2")
    life_support_rating: int = int(oxygen_gen_rating, 2) * int(co2_scrubber_rating, 2)

    print(f"{oxygen_gen_rating = }")
    print(f"{int(oxygen_gen_rating, 2) = }")
    print(f"{co2_scrubber_rating = }")
    print(f"{int(co2_scrubber_rating, 2) = }")
    print(f"{life_support_rating = }")


if __name__ == "__main__":
    main()
