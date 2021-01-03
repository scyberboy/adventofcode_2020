import sys
# import os
import re

my_name = sys.argv[0]
print("my_name:", my_name)
day_nr = re.search(r"\d+", my_name).group()
print("day_nr:", day_nr)


def read_input(input_data):
    for line in sys.stdin:
        _range, _letter, _passwd = line.rstrip().split(" ")
        # input_data.append(line.strip())
        range_min, range_max = _range.split("-")
        letter = _letter.strip(":")
        input_data.append({"range_min": int(range_min),
                           "range_max": int(range_max),
                           "letter": letter,
                           "passwd": _passwd})


def find_sol_a(input_data):
    cnt = 0
    for item in input_data:
        range_min = item['range_min']
        range_max = item['range_max']
        letter = item['letter']
        passwd = item['passwd']

        # reg1 = re.compile("[" + letter + "]" + "{" + str(range_min) + "," + str(range_max) + "}")
        reg1 = re.compile("[" + letter + "]")
        # print(reg1)
        # _found1 = reg1.search(passwd)
        _found1 = reg1.findall(passwd)
        # print(reg1, _found1, passwd)
        if range_min <= len(_found1) <= range_max:
            cnt += 1
        # print(cnt)

    return cnt


def find_sol_b(input_data):
    cnt = 0
    for item in input_data:
        range_min = item['range_min']
        range_max = item['range_max']
        letter = item['letter']
        passwd = item['passwd']

        # reg1 = re.compile("[" + letter + "]" + "{" + str(range_min) + "," + str(range_max) + "}")
        reg1 = re.compile("[" + letter + "]")
        # print(reg1)
        # _found1 = reg1.search(passwd)
        _found1 = reg1.match(passwd, range_min - 1, range_min)
        _found2 = reg1.match(passwd, range_max - 1, range_max)
        # print(reg1, _found1, _found2, passwd)
        # if range_min <= len(_found1) <= range_max:
        if _found1 and not _found2 \
                or not _found1 and _found2:
            cnt += 1
        # print(cnt)

    return cnt


def main():
    global day_nr
    task_day = sys.argv[1] if len(sys.argv) > 1 else 'a'
    my_input = 'd' + day_nr + task_day + ".in"
    print("my_input:", my_input)

    input_data = []
    read_input(input_data)

    # DEBUG
    # print( input_data, end="," )

    nr_correct = find_sol_a(input_data)
    print("answer day{day_nr}({task_day}): {result}".format
          (day_nr=day_nr, task_day="a", result=nr_correct))

    nr_correct = find_sol_b(input_data)
    print("answer day{day_nr}({task_day}): {result}".format
          (day_nr=day_nr, task_day="b", result=nr_correct))


if __name__ == "__main__":
    # execute only if run as a script
    main()
