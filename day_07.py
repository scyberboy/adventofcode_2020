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
    _all = dict()
    # example input:
    # pale turquoise bags contain 3 muted cyan bags, 5 striped teal bags.
    # light tan bags contain 5 posh tomato bags.
    # shiny coral bags contain 2 muted bronze bags.
    # So, try to construct a dictionary with the rules
    for line in sys.stdin:
        # print("line =", line.strip())

        if len(line.split(",")) > 1:
            sp_main, sp_rest = re.split(",", line.strip(), 1)
        else:
            sp_main, sp_rest = line.strip(), None

        # print("sp_main =", sp_main)
        # print("sp_rest =", sp_rest)

        re_main_main = re.search(r"(?P<mcn>^\b.*?\b) bag[s]? contain\s*", sp_main)
        # print(re_main_main)
        # print(re_main_main.groups())
        # print(re_main_main.groupdict())

        # print(sp_main[re_main_main.end():])
        re_main_rest = re.search(r"^\s*(?P<scq>\d+) (?P<scn>.*?) bag[s]?", sp_main[re_main_main.end():])
        # print(re_main_rest)
        # print(re_main_rest.groups())
        # print(re_main_rest.groupdict())

        inner_list_entry = list()

        if re_main_rest:
            inner_list_entry.append([x for x in reversed(re_main_rest.groups())])

        if sp_rest:
            # there's more than 1 secondary colors - process them...
            for x in sp_rest.split(","):
                re_rest = re.search(r"^\s*(?P<scq>\d+) (?P<scn>.*?) bag[s]?", x.strip())
                # print(re_rest)
                # print(re_rest.groups())
                # print(re_rest.groupdict())
                inner_list_entry.append([x for x in reversed(re_rest.groups())])

        # print("inner_list_entry =", inner_list_entry)

        _all[re_main_main.groupdict()["mcn"]] = dict(inner_list_entry)

        # print("_all =", _all)

        # exit(13)

    return _all


def find_sol_a(input_data, my_bag_color):
    global processed_colors_a
    nr_colors = 0
    cont_list = list()

    # print("who contains", my_bag_color, "-> ", end="")

    for k, v in input_data.items():
        if my_bag_color in v:
            cont_list.append(k)
            # print(k, " -> ", v)
            # print(k, end=", ")
            nr_colors += 1

    # print()

    for conter in cont_list:
        if conter in processed_colors_a:
            # print("\t", conter, "is already processed, nr_colors =", processed_colors_a[conter])
            nr_colors -= 1
            continue
        nr_colors += find_sol_a(input_data, conter)

    # print("\tnr_colors for", my_bag_color, "=", nr_colors)
    processed_colors_a[my_bag_color] = nr_colors

    return nr_colors


def find_sol_b(input_data, my_bag_color):
    global processed_colors_b
    total_nr_colors = 0
    my_colors_qty = dict()
    my_colors_score = dict()

    # print(my_bag_color, "contains", "-> ", end="")

    for item in input_data:
        if my_bag_color == item:
            for k, v in input_data[item].items():
                # print(k, " -> ", v)
                # print(v, k, end=", ")
                my_colors_qty[k] = v

    # print()
    # print("my_colors_qty =", pprint.pformat(my_colors_qty))

    for idx, (clr, qty) in enumerate(my_colors_qty.items()):
        # print("{0} my_colors_qty[{1}]".format(my_bag_color, idx), " =>", clr, qty)
        if clr in processed_colors_b:
            # print("\t", clr, "is already processed, nr_colors =", processed_colors_b[clr])
            # tpl = (clr, qty)
            # my_colors_qty.remove(tpl)
            # print("\t", tpl, "removed from my_colors_qty, become =", my_colors_qty)
            continue
        find_sol_b(input_data, clr)

    # print("my_colors_score of", my_bag_color, "=", pprint.pformat(my_colors_score))
    total_nr_colors += sum(int(x) for x in my_colors_qty.values())
    total_nr_colors += sum(int(my_colors_qty[x]) * int(processed_colors_b[x]) for x in my_colors_qty)
    # print("\ttotal_nr_colors of", my_bag_color, "=", total_nr_colors)
    processed_colors_b[my_bag_color] = total_nr_colors

    return total_nr_colors


def main():

    input_data = read_input()
    print("LEN input_data =", len(input_data))
    # print("input_data =", pprint.pformat(input_data))

    nr_correct = find_sol_a(input_data, "shiny gold")
    # print("LEN processed_colors =", len(processed_colors))
    # print("processed_colors =", pprint.pformat(processed_colors))
    print("answer day{day_nr}({task_day}): {result}".format
          (day_nr=day_nr, task_day="a", result=nr_correct))

    nr_correct = find_sol_b(input_data, "shiny gold")
    # print("LEN processed_colors_b =", len(processed_colors_b))
    # print("processed_colors_b =", pprint.pformat(processed_colors_b))
    print("answer day{day_nr}({task_day}): {result}".format
          (day_nr=day_nr, task_day="b", result=nr_correct))


if __name__ == "__main__":
    # execute only if run as a script
    main()
