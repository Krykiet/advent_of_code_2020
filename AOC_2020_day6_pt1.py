with open('day6_input.txt', 'r') as day6_file:
    file_answers = []
    file_lines = day6_file.readlines()
    for line in range(0, len(file_lines)):
        file_answers.append(file_lines[line].strip('\n'))


def sets_of_answers(answers_list):
    total_answers = 0
    answer_dict = dict()
    group_no = 1
    line_counter = 0
    print(len(answers_list))
    for answer in answers_list:
        if answer != '':  # adds entries to dictionary, where key is the group number and value is a set of answers
            if answer_dict.get(group_no) is None:
                # print(f'{answer_dict.get(group_no)} - setting answer for group {group_no}')
                answer_dict[group_no] = set(answer)
                # print(f'{answer_dict.get(group_no)} is now a set of group {group_no}')
                answer_count = len(answer_dict.get(group_no))
                line_counter += 1
            else:
                answer_dict[group_no].update(set(answer))
                # print(f'{answer_dict.get(group_no)} something was here, added more answers for {group_no}')
                answer_count = len(answer_dict.get(group_no))
                line_counter += 1
        else:
            total_answers += answer_count
            # print(f'added answer count for group {group_no}')
            group_no += 1
            line_counter += 1
        if line_counter == len(answers_list):
            total_answers += answer_count
            # print(f'added last answer count for group {group_no}')
    print(total_answers)


sets_of_answers(file_answers)
