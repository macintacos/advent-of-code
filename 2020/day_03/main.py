import math
from typing import List, Tuple

# Real stuff
tree_map = open("2020/day_03/input.txt", "r")
tree_map_list = [line.strip() for line in tree_map.readlines()]

# Test stuff
# tree_map = """..##.......
# #...#...#..
# .#....#..#.
# ..#.#...#.#
# .#...##..#.
# ..#.##.....
# .#.#.#....#
# .#........#
# #.##...#...
# #...##....#
# .#..#...#.#"""
# tree_map_list = tree_map.splitlines()


def calculate_dimensions(tree_map_list: List[str]) -> Tuple[int, int]:
    # Make sure we don't have a weird list
    width: int = 0
    height: int = 0
    lens_of_map_lines = [len(line) for line in tree_map_list]

    # If the list of integers above aren't all equal, "set()" will return a higher value than 1
    valid_map = True if len(set(lens_of_map_lines)) == 1 else False

    if valid_map:
        width = len(tree_map_list[0])
        height = len(tree_map_list)

    return (width, height)


# Determine whether or not we have a map that needs to be extended
def is_map_final(
    map: List[str], map_dimensions: Tuple[int, int], path: Tuple[int, int]
) -> Tuple[bool, int]:
    x_path = path[0]
    y_path = path[1]  # we don't use this yet, maybe we will in the future?
    (map_width, map_height) = map_dimensions

    counter = 0
    for _ in range(map_height):
        counter += x_path

    map_copies_to_make = math.ceil(counter / map_width)

    if map_copies_to_make > 1:
        return (
            False,
            map_copies_to_make,
        )  # We have copies to make, so the map isn't in its "final" state yet

    return (
        True,
        0,
    )  # We don't have copies to make


def extend_map_for_path(tree_map_list: List[str], path: Tuple[int, int]) -> List[str]:
    dimensions = calculate_dimensions(tree_map_list)
    print(f"initial dimensions: {dimensions}")
    (is_final, map_copies) = is_map_final(tree_map_list, dimensions, path)

    new_map: List[str] = []

    if is_final:
        print("okay final")
        return tree_map_list
    else:
        print(f"not final yet, copies to make: {map_copies}")
        # Create a new map with the correct width
        for line in tree_map_list:
            new_line = ""
            for _ in range(map_copies):
                new_line += line

            new_map.append(new_line)
        return new_map


# Determine the amount of collisions
def determine_collisions_for_map(valid_map: List[str], path: Tuple[int, int]):
    print(calculate_dimensions(valid_map))
    counter = 0
    tree_hits = 0
    move_value = path[0]
    for i, line in enumerate(valid_map):
        if i == 0:
            continue
        counter += move_value
        if line[counter] == "#":
            map_marker = "X"
            tree_hits += 1
        else:
            map_marker = "O"
        print(f"----- Line: {line}")
        print(f"Iteration: {i}")
        print(f"Counter: {counter}")
        print(f"Marker: {map_marker}")
        print(f"Tree hits: {tree_hits}")


path_to_traverse = (3, 1)
new_map = extend_map_for_path(tree_map_list, path_to_traverse)
determine_collisions_for_map(new_map, path_to_traverse)

