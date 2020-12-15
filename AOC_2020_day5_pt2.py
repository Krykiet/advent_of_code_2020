with open('day5_input.txt', 'r') as day5_file:
    data = day5_file.readlines()

input_listed = [line.rstrip() for line in data]
seat_id_list = []
row_list = list(range(0,128))  # integers 0-127
seat_list = list(range(0,8))  # integers 0-7
def row_check(input_list):
    for boarding_pass in input_list:
        row_code = boarding_pass[0:7]  # getting 7 first characters
        row_list_token = row_list
        for symbol in row_code:  # dividing the row_list
            if symbol == 'B':
                row_list_token = row_list_token[(len(row_list_token)//2):len(row_list_token)]
            elif symbol == 'F':
                row_list_token = row_list_token[0:len(row_list_token)//2]
        seat_code = boarding_pass[7:]  # getting rest of the characters
        seat_list_token = seat_list
        for symbol in seat_code:  # dividing the seat list
            if symbol == 'R':
                seat_list_token = seat_list_token[(len(seat_list_token) // 2):len(seat_list_token)]
            elif symbol == 'L':
                seat_list_token = seat_list_token[0:len(seat_list_token) // 2]
        seat_id_list.append((row_list_token[0]*8)+seat_list_token[0])

    seat_id_list.sort()
    print(seat_id_list)
    for i in range(0, len(seat_id_list)):
        if seat_id_list[i]+1 != seat_id_list[i+1]:
            print(seat_id_list[i]+1)
            break



row_check(input_listed)