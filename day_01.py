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


def find_2sumup_indexes(data, my_sum):
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            # DEBUG
            # print(i, j, "->", data[i], data[j], "=", data[i] + data[j])
            if data[i] + data[j] == my_sum:
                return i, j
    # if not found, return None
    return None, None


def find_3sumup_indexes(data, my_sum):
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            for k in range(j + 1, len(data)):
                # DEBUG
                # print(i, j, k, "->", data[i], data[j], data[k], "=", data[i] + data[j] + data[k])
                if data[i] + data[j] + data[k] == my_sum:
                    return i, j, k
    # if not found, return None
    return None, None, None


def main():
    global day_nr
    task_day = sys.argv[1] if len(sys.argv) > 1 else 'a'
    my_input = 'd' + day_nr + task_day + ".in"
    print("my_input:", my_input)

    read_input()

    # DEBUG
    # print(input_data, end=",")

    # part 'a' - find 2 numbers that sum up :)
    (idx1, idx2) = find_2sumup_indexes(input_data, 2020)

    # DEBUG
    print(idx1, idx2, "->", input_data[idx1], "*", input_data[idx2], "=", input_data[idx1] * input_data[idx2])
    if idx1 is not None and idx2 is not None:
        print("answer day{day_nr}({task_day}): {result}".format
              (day_nr=day_nr, task_day="a", result=input_data[idx1] * input_data[idx2]))
    else:
        print("No 2 numbers sum-up to 2020...")

    # part 'b' - find 3 numbers that sum up :)
    (idx1, idx2, idx3) = find_3sumup_indexes(input_data, 2020)

    # DEBUG
    print(idx1, idx2, idx3, "->", input_data[idx1], "*", input_data[idx2], "*", input_data[idx3],
          "=", input_data[idx1] * input_data[idx2] * input_data[idx3])
    if idx1 and idx2 and idx3:
        print("answer day{day_nr}({task_day}): {result}".format
              (day_nr=day_nr, task_day="b", result=input_data[idx1] * input_data[idx2] * input_data[idx3]))
    else:
        print("No 3 numbers sum-up to 2020...")


if __name__ == "__main__":
    # execute only if run as a script
    main()
