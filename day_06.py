import sys
import re

my_name = sys.argv[0]
print("my_name:", my_name)
day_nr = re.search(r"\d+", my_name).group()
print("day_nr:", day_nr)


def read_input():
    _all = list()
    group_list = list()

    for line in sys.stdin:
        if line == "\n":
            _all.append(group_list.copy())
            group_list.clear()
            continue

        group_list.append(line.strip())

    _all.append(group_list)

    return _all


def find_sol_a(input_data):
    product = 0

    for item in input_data:
        concat_str = "".join(x for x in item)
        sorted_set = sorted(set(concat_str))
        product += len(sorted_set)

    return product


def find_sol_b(input_data):
    product = 0

    for item in input_data:
        group_list = [x for x in item]
        section_set = set(group_list[0])
        for answers in group_list:
            section_set &= set(answers)

        product += len(section_set)

    return product


def main():

    input_data = read_input()
    # list of lists
    # [
    # ['axft', 'tfxa', 'xtqfa', 'ftqax', 'tgfpax'],
    # ['v', 'h'],
    # ['yf', 'qtp', 'cfzgy', 'lny']
    # ]

    nr_correct = find_sol_a(input_data)
    print("answer day{day_nr}({task_day}): {result}".format
          (day_nr=day_nr, task_day="a", result=nr_correct))

    nr_correct = find_sol_b(input_data)
    print("answer day{day_nr}({task_day}): {result}".format
          (day_nr=day_nr, task_day="b", result=nr_correct))


if __name__ == "__main__":
    # execute only if run as a script
    main()
