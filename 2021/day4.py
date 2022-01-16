"""Day 4."""
from pprint import pprint
from typing import cast

Moves = list[int]
Hits = list[list[int]]
Rows = list[list[int]]
Score = int
Board = dict[str, Hits | Rows | Score]
Boards = list[Board]
"""
A list of boards will kinda look like this:

```
[
    {
        "score": 0,
        "hits": [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
        ],
        "rows": [
            [22, 13, 17, 11,  0],
            [ 8,  2, 23,  4, 24],
            [21,  9, 14, 16,  7],
            [ 6, 10,  3, 18,  5],
            [ 1, 12, 20, 15, 19],
        ]
    }, { etc... ]
]
```
"""


def structure_puzzle_input(is_test=False) -> tuple[Moves, Boards]:
    """Gets the puzzle input."""
    if is_test:
        test_input = [
            "7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1\n",
            "\n",
            "22 13 17 11  0\n",
            " 8  2 23  4 24\n",
            "21  9 14 16  7\n",
            " 6 10  3 18  5\n",
            " 1 12 20 15 19\n",
            "\n",
            " 3 15  0  2 22\n",
            " 9 18 13 17  5\n",
            "19  8  7 25 23\n",
            "20 11 10 24  4\n",
            "14 21 16 12  6\n",
            "\n",
            "14 21 17 24  4\n",
            "10 16 15  9 19\n",
            "18  8 23 26 20\n",
            "22 11 13  6  5\n",
            " 2  0 12  3  7\n",
        ]

        return parse_puzzle_input(test_input)

    input: list[str] = []
    with open("./day_4.txt", "r") as file:
        for line in file:
            input.append(line)

    return parse_puzzle_input(input)


def parse_puzzle_input(puzzle_input: list[str]) -> tuple[Moves, Boards]:  # noqa
    moves: Moves = []
    boards: Boards = []

    # Need to reconstruct the board.
    everything = []
    new_thing = []
    for idx, item in enumerate(puzzle_input):
        if item != "\n":
            new_thing.append(item)
        else:
            # Reset things
            everything.append(new_thing)
            new_thing = []

        if idx + 1 == len(puzzle_input):
            # This is the last board...
            everything.append(new_thing)
            new_thing = []

    # compile moves
    moves = [int(move) for move in everything.pop(0)[0].split(",")]

    # compile the rows in the boards
    every_board: list[list[int]] = []
    for board in everything:
        board_rebuilt = []
        for row in board:
            board_rebuilt.append([int(spot) for spot in row.split()])
        every_board.append(board_rebuilt)

    for board in every_board:
        compiled_metadata = {
            "score": 0,
            "hits": [
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
            ],
            "rows": board,
        }
        boards.append(compiled_metadata)

    return (moves, boards)


def _find_board_hits(move: int, boards: Boards) -> None:
    """NOTE: Mutates the boards that are passed in."""
    print(f"Playing move: {move}")

    for board in boards:
        rows = cast(Rows, board["rows"])
        hits = cast(Hits, board["hits"])

        for idx, row in enumerate(rows):
            try:
                match = row.index(move)
                hits[idx][match] = 1
                board["hits"] = hits
            except ValueError:
                continue
        pprint(board)


def _board_check(hits: Hits) -> bool:
    # Check horizontal winnability
    horizontal_sums = [sum(hit_row) for hit_row in hits]
    if 5 in horizontal_sums:
        print(f"Got a horizontal match: {horizontal_sums.index(5)}")
        return True

    # Check vertical winnability
    transposed_hits = list(map(list, zip(*hits)))
    vertical_sums = [sum(hit_row) for hit_row in transposed_hits]
    if 5 in vertical_sums:
        print(f"Got a vertical match in column: {vertical_sums.index(5)}")
        return True

    return False


def _check_for_winners(boards: Boards) -> list[int]:
    """Checks for the winners in a given round.

    Args:
        boards (Boards): Boards to check.

    Returns:
        list[int]: List of indexes of boards that won the given round.
    """
    print("Checking for a winner...")
    winners: list[int] = []

    for idx, board in enumerate(boards):
        hits = cast(Hits, board["hits"])

        win: bool = _board_check(hits)
        if win:
            winners.append(idx)

    return winners


def _score_board(board: Board, move: int) -> int:
    print(f"Scoring board...")

    # Zero out the places where there are "hits"
    rows = cast(Rows, board["rows"])
    hits = cast(Hits, board["hits"])

    for idx, hit_row in enumerate(hits):
        for idy, hit in enumerate(hit_row):
            if hit == 1:
                rows[idx][idy] = 0

    score: int = sum(sum(rows, [])) * move

    return score


def play_bingo(boards: Boards, moves: Moves) -> None:
    """Plays bingo with the given boards and the list of moves."""
    continue_checking = True
    for idx, move in enumerate(moves):
        if (
            not continue_checking
        ):  # Use this to break out when we've gotten to the last winner.
            break

        print(f"Round: {idx}")
        _find_board_hits(move, boards)
        winners: list[int] = _check_for_winners(boards)
        print(f"{winners = }")

        # Figure out who the last winner is
        if len(winners) != 0:
            prev_winner: int | None = None
            iterations: int = 0
            for winner in winners:
                if len(boards) == 1:
                    print(f"The last winner is board #{winner + 1}!")
                    print(f"Their score is: {_score_board(boards[winner], move)}")

                    # Stop processing.
                    continue_checking = False
                    break
                else:
                    print("We don't care about this winner because it's not the last.")
                    print(
                        f"ELIMINATING: {winner} (note, this is the index of the OG list)"
                    )

                    # Need to make sure that we adjust index properly
                    if prev_winner == None:
                        prev_winner = winner
                        del boards[winner]
                    elif winner > prev_winner:
                        iterations += 1
                        del boards[winner - iterations]
                    elif winner < prev_winner:
                        iterations -= 1
                        del boards[winner + iterations]

        if continue_checking:
            print(f"Unable to find winner for round {idx}.")


def main() -> None:
    """Main thing."""
    input = structure_puzzle_input(is_test=False)
    moves: Moves = input[0]
    boards: Boards = input[1]

    print(f"{len(moves) = }")
    print(f"{moves = }")
    print(f"{len(boards) = }")
    print("Boards:")
    pprint(boards)

    play_bingo(boards, moves)


if __name__ == "__main__":
    main()
