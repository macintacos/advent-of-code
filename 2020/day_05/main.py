import math
from typing import List, Tuple


def binary_seat_search(
    charset: Tuple[str, str], boarding_pass_portion: str, upper: int, lower: int = 0
) -> int:
    """Search for the correct value given the charset and the upper/lower bounds

    :param charset: Character flags that define when to modify upper/lower bound. Define upper flag first, then lower
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


def compute_your_seat(seat_list: List[int]):
    seat_list = sorted(seat_list)

    # Build the theoretical list
    # NOTE: I'm assuming that the first and last values are legit, possible bug for future me?
    lower = seat_list[0]
    upper = seat_list[-1]
    compare_seat_list = list(range(lower, upper))

    # Build sets for comparison purposes
    original_set = set(seat_list)
    compare_set = set(compare_seat_list)

    # Diff the sets, print what's left
    remaining_seats = compare_set.difference(original_set)
    print(remaining_seats)


with open("2020/day_05/input.txt", "r") as file:
    boarding_passes_to_parse = file.read()
    boarding_passes = boarding_passes_to_parse.splitlines()

    highest_id = 0
    seat_list: List[int] = []

    for boarding_pass in boarding_passes:
        row_portion = boarding_pass[:7]
        row = binary_seat_search(("F", "B"), row_portion, upper=127)

        column_portion = boarding_pass[-3:]
        column = binary_seat_search(("L", "R"), column_portion, upper=7)

        seat_id = row * 8 + column
        if seat_id > highest_id:
            highest_id = seat_id

        seat_list.append(seat_id)

    print(f"Highest seat id: {highest_id}")
    compute_your_seat(seat_list)
