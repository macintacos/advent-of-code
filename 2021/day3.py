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


def transpose_strings(binaries: list[str]) -> list[str]:
    """Gets a list of strings and returns a transposed version of it."""
    transposed_strings: list[str] = []

    for i in range(len(binaries[0])):
        new_binary: str = ""
        for j in range(len(binaries)):
            if binaries[j][i] == "\n":
                continue  # skip the newline in the input
            new_binary += binaries[j][i]

        if new_binary == "":
            continue  # skip the newline in the input

        transposed_strings.append(new_binary)

    return transposed_strings


def main() -> None:
    """Does the main things."""
    input: list[str] = puzzle_input(is_test=True)

    gamma_rate: str = ""
    epsilon_rate: str = ""
    oxygen_gen_rating: int = 0
    co2_scrubber_rating: int = 0
    life_support_rating: int = oxygen_gen_rating * co2_scrubber_rating

    input_transposed: list[str] = transpose_strings(input)
    print(f"{len(input_transposed) = }")
    print(f"{input_transposed = }")

    count = 0
    for binary in input_transposed:
        counter = Counter(binary).most_common()

        # To handle unsanitized

        print(f"{counter}")
        gamma_rate += counter[0][0]  # most significant
        epsilon_rate += counter[1][0]  # least significant
        print(f"{count = }")
        count += 1

    print(f"{gamma_rate = }")
    print(f"{int(gamma_rate, 2) = }")
    print(f"{epsilon_rate = }")
    print(f"{int(epsilon_rate, 2) = }")
    print(f"{int(gamma_rate, 2) * int(epsilon_rate, 2) = }")


if __name__ == "__main__":
    main()
