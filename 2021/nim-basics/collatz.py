#!/usr/bin/env python


def collatz_conjecture(input: int) -> int:
    print(input)
    if input == 1:
        return 1  # Break early

    new_input: int

    if input % 2 == 1:
        new_input = input * 3 + 1
    else:
        new_input = int(input / 2)

    return collatz_conjecture(new_input)


collatz_conjecture(670617279)
