passwords = open('day2_input.txt','r')
pass_lines = passwords.readlines()
valid_counter = 0
for line in pass_lines:
    splitted_line = line.split(' ')
    positions = splitted_line[0].split('-')  # getting limits from first item of splitted_line
    pwd = splitted_line[2].rstrip()  # deleting newlines from the last item of splitted_line
    symbol = splitted_line[1][0]  # symbol to check
    position1 = int(positions[0]) - 1
    position2 = int(positions[1]) - 1

    if pwd[position1] == symbol or pwd[position2] == symbol:
        if pwd[position1] == symbol and pwd[position2] == symbol:
            pass
        else:
            valid_counter += 1

print(valid_counter)
