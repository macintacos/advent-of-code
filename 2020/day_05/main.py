import math
from typing import Tuple


def binary_seat_search(
    charset: Tuple[str, str], boarding_pass_portion: str, upper: int, lower: int = 0
) -> int:
    """Search for the correct value given the charset and the upper/lower bounds

    :param charset: Characters that define when to modify upper/lower bound. Define lower flag first, then upper
    :type charset: Tuple[str, str]
    :param lower: Lower bound to start from (typically 0)
    :type lower: int
    :param upper: Upper bound to start from (user-defined)
    :type upper: int
    :return: Returns the value that we found
    :rtype: int
    """

    change_upper_flag = charset[0]
    change_lower_flag = charset[1]

    for char in boarding_pass_portion:
        difference = upper - lower + 1

        if char == change_upper_flag:
            upper -= math.floor(difference / 2)
        elif char == change_lower_flag:
            lower += math.floor(difference / 2)

    if upper == lower:
        return upper

    return lower


def parse_value_from_pass(
    boarding_pass_portion: str, upper_bound: int, directions: Tuple[str, str]
) -> int:
    value: int = 0
    value = binary_seat_search(directions, boarding_pass_portion, upper_bound)

    return value


with open("2020/day_05/input.txt", "r") as file:
    boarding_passes_to_parse = file.read()
    boarding_passes = boarding_passes_to_parse.splitlines()

    highest_id = 0
    for boarding_pass in boarding_passes:
        row_portion = boarding_pass[:7]
        row = parse_value_from_pass(row_portion, upper_bound=127, directions=("F", "B"))

        column_portion = boarding_pass[-3:]
        column = parse_value_from_pass(
            column_portion, upper_bound=8, directions=("L", "R")
        )

        seat_id = row * 8 + column
        if seat_id > highest_id:
            highest_id = seat_id

        print(
            f"For {boarding_pass} -> {row_portion}: {row}, {column_portion}: {column} id: {seat_id}"
        )

    print(f"Highest seat id: {highest_id}")
