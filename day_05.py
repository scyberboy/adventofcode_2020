import sys
import re
import pprint

my_name = sys.argv[0]
print("my_name:", my_name)
day_nr = re.search(r"\d+", my_name).group()
print("day_nr:", day_nr)


def read_input():
    _all = list()

    for line in sys.stdin:
        _all.append(line.strip())

    return _all


def find_binary_repr(letters):
    binary_val = 0
    rev_letters_it = reversed(letters)

    # print("letters =", letters)
    # print("rev_letters =", letters[::-1])

    for idx, letter in enumerate(rev_letters_it):
        if letter in "BR":
            binary_val += pow(2, idx)

        # print(idx, letter, " => ", binary_val)

    return binary_val


def find_sol_a(input_data):
    max_seat_id = 0

    for item in input_data:
        # print("item = ", item)
        row_nr = find_binary_repr(item[:7])
        col_nr = find_binary_repr(item[-3:])
        seat_id = row_nr * 8 + col_nr
        if seat_id > max_seat_id:
            max_seat_id = seat_id

    return max_seat_id


def find_sol_b(input_data):
    my_seat_id = -1
    all_seats_list = list()
    prev_seat_id = -1

    # generate all seat IDs and store them in list
    for item in input_data:
        # print("item = ", item)
        row_nr = find_binary_repr(item[:7])
        col_nr = find_binary_repr(item[-3:])
        seat_id = row_nr * 8 + col_nr
        all_seats_list.append(seat_id)

    all_seats_list.sort()
    # print(all_seats_list)

    # now find a hole in the list (our seat)
    for seat_id in all_seats_list:
        if prev_seat_id != -1:
            if seat_id - prev_seat_id > 1:
                my_seat_id = seat_id - 1
        prev_seat_id = seat_id

    return my_seat_id


def main():
    global day_nr
    task_day = sys.argv[1] if len(sys.argv) > 1 else 'a'
    my_input = 'd' + day_nr + task_day + ".in"
    print("my_input:", my_input)

    input_data = read_input()
    # list of strings "BBBFBFFRLL" (lines)
    # print("LEN input_data =", len(input_data))

    nr_correct = find_sol_a(input_data)
    print("answer day{day_nr}({task_day}): {result}".format
          (day_nr=day_nr, task_day="a", result=nr_correct))

    nr_correct = find_sol_b(input_data)
    print("answer day{day_nr}({task_day}): {result}".format
          (day_nr=day_nr, task_day="b", result=nr_correct))


if __name__ == "__main__":
    # execute only if run as a script
    main()
