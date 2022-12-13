import ast
from functools import cmp_to_key

file = open("day13/input.txt", "r")
contents = file.readlines()


def check_valid(pair):
    i = -1
    list1 = pair[0]
    list2 = pair[1]

    max_lines = max(len(list1), len(list2))
    for i in range(max_lines):
        if i == len(list1) and i < len(list2):
            return True
        if i < len(list1) and i == len(list2):
            return False

        i1 = list1[i]
        i2 = list2[i]

        if isinstance(i1, int):
            if isinstance(i2, int):
                if i1 == i2:
                    continue
                return i1 < i2

            else:
                i1 = [i1]
                new_pair = (i1, i2)

                if check_valid(new_pair) is not None:
                    return check_valid(new_pair)
        else:
            if isinstance(i2, int):
                i2 = [i2]
                new_pair = (i1, i2)
                if check_valid(new_pair) is not None:
                    return check_valid(new_pair)
            else:
                new_pair = (i1, i2)

                if check_valid(new_pair) is not None:
                    return check_valid(new_pair)


def part1():
    pairs = []
    for i in range(0, len(contents)-1, 3):
        line1 = ast.literal_eval(contents[i].strip())
        line2 = ast.literal_eval(contents[i+1].strip())

        pairs.append((line1, line2))

    print(pairs)

    counter = 0
    for p in pairs:
        if check_valid(p):
            counter += pairs.index(p) + 1
            print(pairs.index(p) + 1)
            print(p)

    print(counter)


def part2():
    ls = []
    for i in range(0, len(contents) - 1, 3):
        line1 = ast.literal_eval(contents[i].strip())
        line2 = ast.literal_eval(contents[i + 1].strip())

        ls.append(line1)
        ls.append(line2)

    ls.append([[2]])
    ls.append([[6]])
    ls = sorted(ls, key= cmp_to_key(lambda a,b: -1 if check_valid((a,b)) else 1))
    [print(l) for l in ls]

    a = ls.index([[2]]) + 1
    b = ls.index([[6]]) + 1
    print(a * b)
    counter = 0
    # for p in pairs:
    #     if check_valid(p):
    #         counter += pairs.index(p) + 1
    #         print(pairs.index(p) + 1)
    #         print(p)

    print(counter)


part2()