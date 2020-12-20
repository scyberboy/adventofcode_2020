import sys
# import os
import re

input_data = []

my_name = sys.argv[0]
print("my_name:", my_name)
day_nr = re.search(r"\d+", my_name).group()
print("day_nr:", day_nr)


def read_input():
    for line in sys.stdin:
        input_data.append(int(line.strip()))


def find_sumup_indexes(data, my_sum):
    for i in range(len(data)):
        for j in range(i+1, len(data)):
            # DEBUG
            # print(i, j, "->", data[i], data[j], "=", data[i] + data[j])
            if data[i] + data[j] == my_sum:
                return i, j
    # if not found, return None
    return None, None


def main():
    global day_nr
    task_day = sys.argv[1] if len(sys.argv) > 1 else 'a'
    my_input = 'd' + day_nr + task_day + ".in"
    print("my_input:", my_input)

    read_input()

    # DEBUG
    # print(input_data, end=",")

    # we have the input, now do the job :)
    (idx1, idx2) = find_sumup_indexes(input_data, 2020)

    # DEBUG
    # print(idx1, idx2, "->", input_data[idx1], "*", input_data[idx2], "=", input_data[idx1] * input_data[idx2])
    if idx1 is not None and idx2 is not None:
        print("answer day{day_nr}({task_day}): {result}".format
              (day_nr=day_nr, task_day=task_day, result=input_data[idx1] * input_data[idx2]))
    else:
        print("No numbers sum-up to 2020...")


if __name__ == "__main__":
    # execute only if run as a script
    main()
