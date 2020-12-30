import sys
import re
import pprint

my_name = sys.argv[0]
print("my_name:", my_name)
day_nr = re.search(r"\d+", my_name).group()
print("day_nr:", day_nr)

processed_colors_a = dict()
processed_colors_b = dict()


def read_input():
    _all = list()

    for line in sys.stdin:
        _cmd, _arg = line.strip().split()
        _all.append((_cmd, int(_arg)))

    return _all


def find_sol_a(input_data):
    accumulator = 0
    instr_set = dict()
    idx = 0

    while True:
        _cmd, _val = input_data[idx]

        # print(idx, accumulator, _cmd, _val)

        if instr_set.get(idx) is None:
            instr_set[idx] = 'x'
        else:
            break

        if _cmd == "jmp":
            idx += _val
            continue
        elif _cmd == "acc":
            accumulator += _val
            idx += 1
            continue
        else:  # it should be nop
            idx += 1
            continue

    return accumulator


def find_sol_b(input_data):
    nr_potential_subs = list()
    all_processed = False
    final_accumulator = 0

    for i in range(len(input_data)):
        if input_data[i][0] in "jmp nop":
            nr_potential_subs.append(i)

    # print("LEN nr_potential_subs", len(nr_potential_subs))
    # print(nr_potential_subs)

    for i in nr_potential_subs:
        new_input = input_data.copy()
        tpl = ("nop" if new_input[i][0] == "jmp" else "jmp", new_input[i][1])
        new_input[i] = tpl

        accumulator = 0
        instr_set = dict()
        idx = 0
        prev_idx = 0

        if all_processed:
            break

        # print("TRY", i)

        while not all_processed:

            if idx >= len(new_input):
                # print("ALL processed - finish!")
                all_processed = True
                final_accumulator = accumulator
                break

            _cmd, _val = new_input[idx]
            _prev_cmd, _prev_val = new_input[prev_idx]

            # print(idx, accumulator, _cmd, _val)

            cur_instr_set = instr_set.get(idx)
            if cur_instr_set is None:
                instr_set[idx] = 'x'
            else:
                break

            if _cmd == "jmp":
                prev_idx = idx
                idx += _val
                continue
            elif _cmd == "acc":
                accumulator += _val
                prev_idx = idx
                idx += 1
                continue
            else:  # it should be nop
                prev_idx = idx
                idx += 1
                continue

    return final_accumulator


def main():

    input_data = read_input()
    # print("LEN input_data =", len(input_data))
    # print("input_data =", pprint.pformat(input_data))

    nr_correct = find_sol_a(input_data)
    # print("LEN processed_colors =", len(processed_colors))
    # print("processed_colors =", pprint.pformat(processed_colors))
    print("answer day{day_nr}({task_day}): {result}".format
          (day_nr=day_nr, task_day="a", result=nr_correct))

    nr_correct = find_sol_b(input_data)
    # print("LEN processed_colors_b =", len(processed_colors_b))
    # print("processed_colors_b =", pprint.pformat(processed_colors_b))
    print("answer day{day_nr}({task_day}): {result}".format
          (day_nr=day_nr, task_day="b", result=nr_correct))


if __name__ == "__main__":
    # execute only if run as a script
    main()
