input = open("2020/day_02/input.txt")
input_lines = input.readlines()
# input_lines = ["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"]


def validate_password(policy: str, password: str) -> bool:
    # Parse the policy
    scoped_char: str = policy.split(" ")[1]
    min_max_value: str = policy.split(" ")[0]
    min_value: int = int(min_max_value.split("-")[0])
    max_value: int = int(min_max_value.split("-")[1])

    # print("Validating...")
    # print(
    #     f"character: {scoped_char}, min: {min_value}, max: {max_value}, password: {password}"
    # )

    # Begin comparison
    count: int = 0
    for char in password:
        if char == scoped_char:
            count += 1

    if count < min_value or count > max_value:
        # Failed
        return False

    return True


good_password_count: int = 0
for line in input_lines:
    original_line = line.split(":")

    policy: str = original_line[0]
    password: str = original_line[1].strip()
    test_decision: bool = validate_password(policy, password)
    # print(f"Test decision: {test_decision}")

    if test_decision:
        good_password_count += 1

print(f"Number of passwords tested: {len(input_lines)}")
print(f"Number of passwords failed: {good_password_count}")
