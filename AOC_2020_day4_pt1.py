with open('day4_input.txt', 'r') as f:
    data = f.readlines()
    input_listed = []
    for line in data:
        input_listed = [line.strip() for line in data]  # read input file line-by-line into a list

def valid_passports(list_of_passports):
    valid_passport_req = ['eyr', 'hgt', 'hcl', 'ecl', 'pid', 'byr', 'iyr']
    valid_passports = 0
    passport_fields = []
    for passport in list_of_passports:
        if passport == '':  # if we have new passport coming we check the previous (file begins with blank line):
            if all(field in passport_fields for field in valid_passport_req):
                # if all fields in passports meet the requirements
                valid_passports += 1
            passport_fields = []
        else:
            for value in passport.split():  #
                passport_fields.append(value.split(':')[0])  # adds values splitted by : and 1st item from them to list
    print(valid_passports)

valid_passports(input_listed)