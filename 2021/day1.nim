import std/math
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

proc parseSlidingInput(input: seq[int]) =
    var
        current_iteration = 0
        deconstructed_measures: seq[seq[int]]

    for i in input:
        var
            beginning = current_iteration
            ending = block:
                if len(input) > current_iteration + 2:
                    current_iteration + 2
                else: continue # just skip these last iterations

        deconstructed_measures.add(input[beginning..ending])
        current_iteration += 1

    var
        last_sum = 0
        count_increases = 0
    for idx, measures in deconstructed_measures:
        if idx == 0: # skip first iteration
            echo fmt"{idx} is the starting iteration."
            continue

        var current_sum = sum(measures)
        if current_sum > last_sum:
            echo fmt"{idx}: {current_sum} is greater than {last_sum}"
            count_increases += 1
        else:
            echo fmt"{idx}: {current_sum} is lower than {last_sum}"
        last_sum = current_sum

    echo fmt"There were '{count_increases}' increases."

parseInput(readInput())
parseSlidingInput(readInput())
