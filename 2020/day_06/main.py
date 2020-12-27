from typing import List, Set


def merge_answers_for_group(group: List[str]) -> Set[str]:
    merged_answer_set = set([answer for answers in group for answer in answers])

    return merged_answer_set


with open("./input.txt", "r") as file:
    content = file.read()
    group_answers = content.split("\n\n")

    num_yes_answers_per_group: List[int] = []
    for index, group in enumerate(group_answers):
        # Merge all of the answers into one set of answers
        # Sum the counts of "yes" answers
        group_split = group.splitlines()
        merged_answers = merge_answers_for_group(group_split)
        num_yes_answers_per_group.append(len(merged_answers))

    print(f"Number of yes answers in all groups: {sum(num_yes_answers_per_group)}")
