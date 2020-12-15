with open('day6_input.txt', 'r') as day6_file:
    file_answers = []
    file_lines = day6_file.readlines()
    for line in range(0, len(file_lines)):
        file_answers.append(file_lines[line].strip('\n'))


def sets_of_answers(answers_list):
    answer_dict = dict()
    group_no = 1
    line_counter = 0
    all_answered = 0
    print(len(answers_list))
    for answer in answers_list:
        if answer != '':  # adds entries to dictionary, where key is the group number and value is a set of answers
            if answer_dict.get(group_no) is None:
                answer_dict[group_no] = list(answer)
                line_counter += 1
                people_in_group = 1
                # print(people_in_group)
            else:
                answer_dict[group_no].extend(list(answer))
                line_counter += 1
                people_in_group += 1
                # print(people_in_group)
        if answer == '':
            if people_in_group == 1:
                all_answered += len(answer_dict.get(group_no))
                people_in_group = 0
            else:
                all_in_group_answered = 0
                seen = list()
                for i in answer_dict.get(group_no):
                    if answer_dict.get(group_no).count(i) == people_in_group:
                        if i not in seen:
                            seen.append(i)
                            all_in_group_answered += 1
                all_answered += all_in_group_answered
                print(f'added {people_in_group} people')
                people_in_group = 0
            group_no += 1
            line_counter += 1
        if line_counter == len(answers_list):
            if people_in_group == 1:
                all_answered += len(answer_dict.get(group_no))
                people_in_group = 0
            else:
                all_in_group_answered = 0
                seen = list()
                for i in answer_dict.get(group_no):
                    if answer_dict.get(group_no).count(i) == people_in_group:
                        if i not in seen:
                            seen.append(i)
                            all_in_group_answered += 1
                all_answered += all_in_group_answered
                print(f'added {people_in_group} people')
                people_in_group = 0
    print(all_answered)


sets_of_answers(file_answers)
