import sys
import re

my_name = sys.argv[0]
print("my_name:", my_name)
day_nr = re.search(r"\d+", my_name).group()
print("day_nr:", day_nr)


def read_input():
    _all = list()
    for line in sys.stdin:
        _all.append(line.strip())

    return _all


def find_sol_a(input_data):
    _inc_hor = 3
    _inc_ver = 1
    _limit_hor = len(input_data[0])
    _limit_ver = len(input_data)
    _cnt_tree = 0
    _fld_free = "."
    _fld_tree = "#"
    _pos_hor = 0
    _pos_ver = 0

    while True:
        _pos_hor += _inc_hor
        # keep the horizontal index in limit (modulo)
        _pos_hor = _pos_hor % _limit_hor
        _pos_ver += _inc_ver

        # limit statement
        if _pos_ver >= _limit_ver:
            break

        if input_data[_pos_ver][_pos_hor] == _fld_tree:
            _cnt_tree += 1

    return _cnt_tree


def find_sol_b(input_data, _inc_hor, _inc_ver):
    _limit_hor = len(input_data[0])
    _limit_ver = len(input_data)
    _cnt_tree = 0
    _fld_free = "."
    _fld_tree = "#"
    _pos_hor = 0
    _pos_ver = 0

    while True:
        _pos_hor += _inc_hor
        # keep the horizontal index in limit (modulo)
        _pos_hor = _pos_hor % _limit_hor
        _pos_ver += _inc_ver

        # limit statement
        if _pos_ver >= _limit_ver:
            break

        if input_data[_pos_ver][_pos_hor] == _fld_tree:
            _cnt_tree += 1

    return _cnt_tree


def main():
    global day_nr
    task_day = sys.argv[1] if len(sys.argv) > 1 else 'a'
    my_input = 'd' + day_nr + task_day + ".in"
    print("my_input:", my_input)

    input_data = read_input()
    # it's a list of strings... but luckily accessible like two-dimensional array :)

    nr_correct = find_sol_a(input_data)
    print("answer day{day_nr}({task_day}): {result}".format
          (day_nr=day_nr, task_day="a", result=nr_correct))

    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    product = 1
    for j, i in slopes:
        nr_correct = find_sol_b(input_data, j, i)
        product *= nr_correct
    print("answer day{day_nr}({task_day}): {result}".format
          (day_nr=day_nr, task_day="b", result=product))


if __name__ == "__main__":
    # execute only if run as a script
    main()
