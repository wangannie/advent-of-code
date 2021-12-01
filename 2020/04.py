import re

fields = ('eyr', 'hgt', 'hcl', 'pid', 'byr', 'ecl', 'iyr')
eye_colors = ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')


def valid_fields(passport):
    for f in fields:
        if f not in passport:
            return False
    return True


def valid_num_in_range(passport_dict, field, at_least, at_most):
    if not passport_dict[field].isdigit():
        return False
    val = int(passport_dict[field])
    return val >= at_least and val <= at_most


def valid_height(input):
    if 'cm' in input and input[:-2].isdigit():
        hgt = int(input[:-2])
        return hgt >= 150 and hgt <= 193
    if 'in' in input and input[:-2].isdigit():
        hgt = int(input[:-2])
        return hgt >= 59 and hgt <= 76
    return False


def passport_to_dict(passport):
    passport = passport.replace('\n', ' ').split(' ')
    passport_dict = {}
    for field in passport:
        field_name, field_val = field.split(':')
        passport_dict[field_name] = field_val
    return passport_dict


def valid_values(passport):
    passport_dict = passport_to_dict(passport)
    byr = valid_num_in_range(passport_dict, 'byr', 1920, 2002)
    iyr = valid_num_in_range(passport_dict, 'iyr', 2010, 2020)
    eyr = valid_num_in_range(passport_dict, 'eyr', 2020, 2030)
    hgt = valid_height(passport_dict['hgt'])
    hcl = bool(re.match(r'^#(?:[0-9a-fA-F]{3}){1,2}$', passport_dict['hcl']))
    ecl = passport_dict['ecl'] in eye_colors
    pid = passport_dict['pid'].isdigit() and len(passport_dict['pid']) == 9
    return byr and iyr and eyr and hgt and hcl and ecl and pid


def part1(data):
    rows = [n for n in data.split('\n\n')]
    num_valid = 0
    for r in rows:
        num_valid += valid_fields(r)
    return num_valid


def part2(data):
    rows = [n for n in data.split('\n\n')]
    num_valid = 0
    for r in rows:
        num_valid += valid_fields(r) and valid_values(r)
    return num_valid


# byr (Birth Year) - four digits; at least 1920 and at most 2002.
# iyr (Issue Year) - four digits; at least 2010 and at most 2020.
# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.

# hgt (Height) - a number followed by either cm or in:
# If cm, the number must be at least 150 and at most 193.
# If in, the number must be at least 59 and at most 76.

# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.

# pid (Passport ID) - a nine-digit number, including leading zeroes.
# cid (Country ID) - ignored, missing or not.
