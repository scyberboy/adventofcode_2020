import sys
import re
import pprint
import itertools


my_name = sys.argv[0]
print("my_name:", my_name)
day_nr = re.search(r"\d+", my_name).group()
print("day_nr:", day_nr)

processed_colors_a = dict()
processed_colors_b = dict()


def read_input():
    _all = list()

    for line in sys.stdin:
        _all.append(int(line.strip()))

    return _all


def is_conformer(num, nums):
    _res = False
    for i in range(len(nums)-1):
        if _res:
            break
        for j in range(i+1, len(nums)):
            if num == nums[i] + nums[j]:
                _res = True
                break

    return _res


def find_sol_a(input_data):
    non_conformer = -1
    nr_preamble = 25

    for idx in range(nr_preamble, len(input_data)):
        idx_from = idx - nr_preamble
        idx_to = idx
        cur_num = input_data[idx]
        if not is_conformer(cur_num, input_data[idx_from:idx_to]):
            non_conformer = cur_num
            break

    return non_conformer


def gen_cont_lists(reduced_data_set, nr_addend):
    _all = list()
    for i in range(len(reduced_data_set) - nr_addend + 1):
        _all.append(reduced_data_set[i:i+nr_addend])

    return _all


def find_sol_b(input_data, invalid_nr):
    _res = -1
    _all_sums = dict()
    init_nr_addents = 2

    reduced_data_set = input_data[:input_data.index(invalid_nr)]
    # print("INIT reduced set,", len(reduced_data_set))
    # pprint.pprint(reduced_data_set)

    for nr_addend in range(init_nr_addents, len(reduced_data_set)+1):
        # print("nr_addend =>", nr_addend)
        _lists = gen_cont_lists(reduced_data_set, nr_addend)
        for _inner_list in _lists:
            # print(len(_inner_list), " -> ", _inner_list)
            _sum = sum(x for x in _inner_list)
            _all_sums[_sum] = _inner_list
            # print("\tsum =", _sum)
            if invalid_nr == _sum:
                _inner_list.sort()
                _res = _inner_list[0] + _inner_list[-1]
                # print(_sum, "found it ->", _inner_list, _res)
                return _res

    print("FINAL ALL sums:")
    # _all_sums.sort()
    pprint.pprint(_all_sums)

    return _res


def main():

    input_data = read_input()
    # print("LEN input_data =", len(input_data))
    # print("input_data =", pprint.pformat(input_data))

    nr_correct = find_sol_a(input_data)
    # print("LEN processed_colors =", len(processed_colors))
    # print("processed_colors =", pprint.pformat(processed_colors))
    print("answer day{day_nr}({task_day}): {result}".format
          (day_nr=day_nr, task_day="a", result=nr_correct))

    nr_correct = find_sol_b(input_data, nr_correct)
    # print("LEN processed_colors_b =", len(processed_colors_b))
    # print("processed_colors_b =", pprint.pformat(processed_colors_b))
    print("answer day{day_nr}({task_day}): {result}".format
          (day_nr=day_nr, task_day="b", result=nr_correct))


if __name__ == "__main__":
    # execute only if run as a script
    main()
