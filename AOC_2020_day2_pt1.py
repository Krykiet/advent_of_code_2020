passwords = open('day2_input.txt','r')
pass_lines = passwords.readlines()
pass_splitted = []
valid_counter = 0
for line in pass_lines:
    splitted_line = line.split(' ')
    limits_line = splitted_line[0].split('-')  # getting limits from first item of splitted_line
    splitted_line[0] = limits_line
    stripped_pass = splitted_line[2].rstrip()  # deleting newlines from the last item of splitted_line
    splitted_line[2] = stripped_pass

    pass_splitted.append(splitted_line)  # just for chcecking purposes, can be deleted
    character = splitted_line[1][0]
    counter = splitted_line[2].count(character)
    lower = int(splitted_line[0][0])
    upper = int(splitted_line[0][1])
    print(lower, counter, upper, valid_counter)  # also just for checking, can be deleted

    if lower <= counter <= upper:
        valid_counter += 1

print(pass_splitted)  # just for checking, can be deleted
print(valid_counter)