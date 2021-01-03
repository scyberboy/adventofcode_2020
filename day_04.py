import sys
import re
import pprint

my_name = sys.argv[0]
print("my_name:", my_name)
day_nr = re.search(r"\d+", my_name).group()
print("day_nr:", day_nr)


def read_input():
    _all = list()
    _entry_dict = None
    _keys = list()
    _values = list()

    for line in sys.stdin:

        if line == "\n":
            _entry_dict = dict(zip(_keys, _values))
            # print("_entry_dict =", _entry_dict)
            _keys.clear()
            _values.clear()
            # print("_keys =", _keys)
            # print("_values =", _values)
            _all.append(_entry_dict)

        # blah...
        # print("line =", line, end="")
        # _entry_list.append([x for x in line.strip().split(": ")])
        for chunk in line.strip().split():
            # print("chunk =", chunk)
            k, v = chunk.split(":")
            _keys.append(k)
            _values.append(v)
        # print("_keys =", _keys)
        # print("_values =", _values)

    _entry_dict = dict(zip(_keys, _values))
    # print("_entry_dict =", _entry_dict)
    _all.append(_entry_dict)

    return _all


def find_sol_a(input_data):
    _cnt_valid = 0
    _min_nr_fields = 8
    _optional_field = "cid"
    # to be valid, a passport should have 8 fields.
    # <cid> is optional, all the rest are required.
    # So if they are < 8, the missing one should be <cid>

    for dict_item in input_data:
        _is_valid = True

        if len(dict_item) < _min_nr_fields - 1:
            _is_valid = False
        elif len(dict_item) < _min_nr_fields \
                and _optional_field in dict_item:
            _is_valid = False
        # in all other cases it's True (default) :)

        if _is_valid:
            _cnt_valid += 1

    return _cnt_valid


def validate_fields(dict_item):
    # Additionally, all fields should comply to the following rules:
    # byr (Birth Year) - four digits; at least 1920 and at most 2002.
    # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    # hgt (Height) - a number followed by either cm or in:
    #   If cm, the number must be at least 150 and at most 193.
    #   If in, the number must be at least 59 and at most 76.
    # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    # pid (Passport ID) - a nine-digit number, including leading zeroes.
    # cid (Country ID) - ignored, missing or not.
    _is_valid = True

    # print(dict_item)

    byr = int(re.search(r"^\d{4}$", dict_item["byr"]).group())
    iyr = int(re.search(r"^\d{4}$", dict_item["iyr"]).group())
    eyr = int(re.search(r"^\d{4}$", dict_item["eyr"]).group())
    hgt_val = int(re.search(r"^\d+", dict_item["hgt"]).group())
    hgt_unit = re.search(r"(cm|in)$", dict_item["hgt"]).group() if re.search(r"(cm|in)$", dict_item["hgt"]) else "none"
    hcl = re.search(r"^#[0-9a-f]{6}$", dict_item["hcl"])
    ecl = dict_item["ecl"]
    pid = re.search(r"^\d{9}$", dict_item["pid"])

    if byr < 1920 or byr > 2002:
        _is_valid = False
    elif iyr < 2010 or iyr > 2020:
        _is_valid = False
    elif eyr < 2020 or eyr > 2030:
        _is_valid = False
    elif (hgt_unit == "cm" and (hgt_val < 150 or hgt_val > 193)) \
            or (hgt_unit == "in" and (hgt_val < 59 or hgt_val > 76)) \
            or hgt_unit == "none":
        _is_valid = False
    elif not hcl:
        _is_valid = False
    elif ecl not in "amb blu brn gry grn hzl oth":
        _is_valid = False
    elif not pid:
        _is_valid = False
    else:
        _is_valid = True

    return _is_valid


def find_sol_b(input_data):
    _cnt_valid = 0
    _min_nr_fields = 8
    _optional_field = "cid"
    _all_fields_valid = True
    # to be valid, a passport should have 8 fields.
    # <cid> is optional, all the rest are required.
    # So if they are < 8, the missing one should be <cid>

    for dict_item in input_data:
        _is_valid = True

        if len(dict_item) < _min_nr_fields - 1:
            _is_valid = False
        elif len(dict_item) < _min_nr_fields \
                and _optional_field in dict_item:
            _is_valid = False
        # in all other cases it's True (default) :)

        if _is_valid:
            _all_fields_valid = validate_fields(dict_item)
            if _all_fields_valid:
                _cnt_valid += 1

    return _cnt_valid


def main():
    global day_nr
    task_day = sys.argv[1] if len(sys.argv) > 1 else 'a'
    my_input = 'd' + day_nr + task_day + ".in"
    print("my_input:", my_input)

    input_data = read_input()
    # list of dictionaries
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
