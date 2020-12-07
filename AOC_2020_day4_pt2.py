import re

# regular expressions for passport requirements
byr_pattern = re.compile(r"^(19[2-9][0-9]|200[0-2])$")
iyr_pattern = re.compile(r"^(201[0-9]|2020)$")
eyr_pattern = re.compile(r"^(202[0-9]|2030)$")
hgt_pattern = re.compile(r"^(59in|6[0-9]in|7[0-6]in|1[5-8][0-9]cm|19[0-3]cm)$")
hcl_pattern = re.compile(r"^(#[(0-9a-f)]{6})")
ecl_pattern = re.compile(r"^(amb|blu|brn|gry|grn|hzl|oth)$")
pid_pattern = re.compile(r"^([0-9]{9})")

with open('day4_input.txt', 'r') as file:
    data = file.readlines()
    input_listed = []
    for line in data:
        input_listed = [line.strip() for line in data]  # read input file line-by-line into a list


def valid_passports(list_of_passports):
    valid_passport_req = ['eyr', 'hgt', 'hcl', 'ecl', 'pid', 'byr', 'iyr']
    valid_passports = 0
    passport_fields = dict()  # dict for checking the values
    for passport in list_of_passports:
        print(passport, valid_passports)
        if all(field in passport_fields for field in valid_passport_req):
            if bool(byr_pattern.fullmatch(passport_fields.get('byr'))):
                if bool(iyr_pattern.fullmatch(passport_fields.get('iyr'))):
                    if bool(eyr_pattern.fullmatch(passport_fields.get('eyr'))):
                        if bool(hgt_pattern.fullmatch(passport_fields.get('hgt'))):
                            if bool(hcl_pattern.fullmatch(passport_fields.get('hcl'))):
                                if bool(ecl_pattern.fullmatch(passport_fields.get('ecl'))):
                                    if bool(pid_pattern.fullmatch(passport_fields.get('pid'))):
                                        valid_passports += 1
            passport_fields = dict()
        else:
            for value in passport.split():
                key = value.split(':')[0]
                val = value.split(':')[1]
                passport_fields[key] = val   # adds values splitted by : and 1st item from them to list
    # to apply the same to the last:
    for value in passport.split():
        key = value.split(':')[0]
        val = value.split(':')[1]
        passport_fields[key] = val  # adds values splitted by : and 1st item from them to list
    if all(field in passport_fields for field in valid_passport_req):
        if bool(byr_pattern.fullmatch(passport_fields.get('byr'))):
            if bool(iyr_pattern.fullmatch(passport_fields.get('iyr'))):
                if bool(eyr_pattern.fullmatch(passport_fields.get('eyr'))):
                    if bool(hgt_pattern.fullmatch(passport_fields.get('hgt'))):
                        if bool(hcl_pattern.fullmatch(passport_fields.get('hcl'))):
                            if bool(ecl_pattern.fullmatch(passport_fields.get('ecl'))):
                                if bool(pid_pattern.fullmatch(passport_fields.get('pid'))):
                                    valid_passports += 1
    print(valid_passports)


valid_passports(input_listed)
