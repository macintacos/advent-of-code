import std/strformat
import strutils

var
    test_input = @[199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
    previous: int
    count_increases: int

proc readInput(): seq[int] =
    var res: seq[int]

    for line in lines "day1_input.txt":
        res.add(line.parseInt)

    return res


proc parseInput(input: seq[int]) =
    for idx, val in input:
        if idx == 0: # skip first iteration
            echo fmt"{val} is the starting val."
            continue
        if val > previous:
            echo fmt"{val} is greater than {previous}"
            count_increases += 1
        else: echo fmt"{val} is lower than {previous}"
        previous = val

    echo fmt"There were '{count_increases}' increases."

parseInput(readInput())

