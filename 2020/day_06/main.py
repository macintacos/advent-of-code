from typing import List, Set


def merge_answers_for_group(group: List[str]) -> Set[str]:
    merged_answer_set = set([answer for answers in group for answer in answers])

    return merged_answer_set


def get_group_answer_intersection(group: List[str]) -> Set[str]:
    group_sets = map(set, group)
    merge_answers_for_group = set.intersection(*group_sets)

    return merge_answers_for_group


with open("./input.txt", "r") as file:
    content = file.read()
    group_answers = content.split("\n\n")

    num_yes_merged_answers_per_group: List[int] = []
    num_yes_intersection_answers_per_group: List[int] = []

    for group in group_answers:
        group_split = group.splitlines()
        merged_answers = merge_answers_for_group(group_split)
        intersection_answers = get_group_answer_intersection(group_split)

        num_yes_merged_answers_per_group.append(len(merged_answers))
        num_yes_intersection_answers_per_group.append(len(intersection_answers))

    print(
        f"Number of yes answers in merged groups: {sum(num_yes_merged_answers_per_group)}"
    )
    print(
        f"Number of yes answers in intersected groups: {sum(num_yes_intersection_answers_per_group)}"
    )
