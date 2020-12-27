import re
from typing import Dict, List

VALID_FIELDS = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
OPTIONAL_FIELD = "cid"

# Take a passport string and convert it to valid json and then to a python dictionary
def convert_passport_to_dict(passport: str) -> Dict[str, str]:
    passport = passport.replace("\n", " ")

    converted_passport = dict(
        (x.strip(), y.strip())
        for x, y in (element.split(":") for element in passport.split(" "))
    )

    return converted_passport


# Check the dictionary to make sure all of the fields are there (we can ignore `cid` if it's not there)
def is_passport_valid(passport: Dict[str, str]) -> bool:
    checklist: List[bool] = []

    for field_and_value in passport.items():
        field = field_and_value[0]
        value = field_and_value[1]

        if field not in VALID_FIELDS:
            if field not in OPTIONAL_FIELD:
                checklist.append(False)
                continue
            continue  # we aren't appending the result of the optional field here because... it's optional

        test_field_result = is_field_value_valid(field, value)

        checklist.append(test_field_result)

    if len(checklist) < len(VALID_FIELDS):
        return False  # assume we don't have a good set if we don't even have the right amount of values to compare

    for result in checklist:
        if result == False:
            return False

    return True


def is_field_value_valid(field: str, value: str) -> bool:
    (byr, iyr, eyr, hgt, hcl, ecl, pid) = VALID_FIELDS

    if byr == field:
        if len(value) > 4 or len(value) < 4 or int(value) < 1920 or int(value) > 2002:
            return False

    elif iyr == field:
        if len(value) > 4 or len(value) < 4 or int(value) < 2010 or int(value) > 2020:
            return False

    elif eyr == field:
        if len(value) > 4 or len(value) < 4 or int(value) < 2020 or int(value) > 2030:
            return False

    elif hgt == field:
        if "cm" not in value and "in" not in value:
            return False
        if "cm" in value:
            value = value.replace("cm", "")
            if int(value) < 150 or int(value) > 193:
                return False
        if "in" in value:
            value = value.replace("in", "")
            if int(value) < 59 or int(value) > 76:
                return False

    elif hcl == field:
        prog = re.compile(r"^#[a-f0-9]{6}$")
        if prog.match(value):
            return True
        else:
            return False

    elif ecl == field:
        valid_colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
        if value not in valid_colors:
            return False

    elif pid == field:
        prog = re.compile(r"^[0-9]{9}$")
        if prog.match(value):
            return True
        else:
            return False

    else:
        print(f"Tried to check {field}: {value}")
        return False

    return True


with open("./input.txt", "r") as file:
    passports_to_validate = file.read()

    # Split out the passports based on newlines
    passport_validation_list = passports_to_validate.split("\n\n")

    valid_passport_counter = 0
    for passport in passport_validation_list:
        converted_passport = convert_passport_to_dict(passport)
        valid = is_passport_valid(converted_passport)

        if valid:
            print(converted_passport)
            valid_passport_counter += 1
        else:
            print(f"Invalid passport: {converted_passport}")

    print(f"Valid passports scanned: {valid_passport_counter}")
