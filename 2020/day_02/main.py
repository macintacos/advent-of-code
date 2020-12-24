input = open("2020/day_02/input.txt")
input_lines = input.readlines()
# input_lines = ["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"]


def validate_password(policy: str, password: str) -> bool:
    # Parse the policy
    scoped_char: str = policy.split(" ")[1]

    positioning_values: str = policy.split(" ")[0]
    first_position: int = int(positioning_values.split("-")[0]) - 1
    second_position: int = int(positioning_values.split("-")[1]) - 1

    print("Validating...")
    print(
        f"character: {scoped_char}, first: {first_position}, second: {second_position}, password: {password}"
    )

    # Begin comparison
    password_chars = [char for char in password]
    char_first_position: str = password_chars[first_position]
    char_second_position: str = password_chars[second_position]
    print(f"1st char: {char_first_position}, 2nd char: {char_second_position}")
    print(f"1st compare: '{char_first_position}' : '{scoped_char}'")
    print(f"2nd compare: '{char_second_position}' : '{scoped_char}'")

    if (
        char_first_position == scoped_char and not char_second_position == scoped_char
    ) or (
        char_second_position == scoped_char and not char_first_position == scoped_char
    ):
        return True
    return False



good_password_count: int = 0
for line in input_lines:
    original_line = line.split(":")

    policy: str = original_line[0]
    password: str = original_line[1].strip()
    test_decision: bool = validate_password(policy, password)
    print(f"Test decision: {test_decision}")

    if test_decision:
        good_password_count += 1

print(f"Number of passwords tested: {len(input_lines)}")
print(f"Number of passwords valid: {good_password_count}")
