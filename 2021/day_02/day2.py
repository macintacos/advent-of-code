"""Day 2."""
import sys


def parse_input(is_test = False) -> list[str]:
    """Gets the test input."""
    if is_test:
        return [
            "forward 5",
            "down 5",
            "forward 8",
            "up 3",
            "down 8",
            "forward 2",
        ]

    input: list[str] = []
    with open("./day_2.txt", "r") as file:
        for line in file:
            input.append(line)

    return input

def run() -> None:  # noqa
    test_instructions: list[str] = parse_input()

    aim: int = 0
    depth: int = 0
    horizontal_pos: int = 0
    parsed_instructions: list[tuple[str, int]] = []

    # Get the instruction and the amount
    for instruction in test_instructions:
        split = instruction.split()
        instruction = split[0]
        amount = int(split[1])
        parsed_instructions.append((instruction, amount))

    # Figure out where to go
    for instruction in parsed_instructions:
        command: str = instruction[0]
        amount: int = instruction[1]

        match command:
            case "forward":
                horizontal_pos += amount
                depth += amount * aim
            case "down":
                aim += amount
            case "up":
                aim -= amount
            case _:
                print("got an instruction that we didn't expect!")
                sys.exit(1)

    print(f"{horizontal_pos = }, {depth = }")
    print(f"{horizontal_pos * depth = }")


if __name__ == "__main__":
    run()
