file = open("day1/input.txt", "r")
contents = file.readlines()


def part1():
    elf = []
    index = 0
    i = 0
    while i < (len(contents)):
        elf.append(0)
        for j in range(i, len(contents)):
            if contents[j].isspace():
                print(index)
                i = j
                index += 1
                break
            else:
                print(contents[j].strip())
                elf[index] += int(contents[j].strip())
        i += 1
        print()
    print(elf)

    elf.sort()
    print(elf[len(elf) - 1])

    # print(elf)


def part2():
    elf = []
    index = 0
    i = 0
    while i < (len(contents)):
        elf.append(0)
        for j in range(i, len(contents)):
            if contents[j].isspace():
                print(index)
                i = j
                index += 1
                break
            else:
                print(contents[j].strip())
                elf[index] += int(contents[j].strip())
        i += 1
        print()
    print(elf)

    elf.sort()
    print(elf[len(elf) - 1] + elf[len(elf) - 2] + elf[len(elf) - 3])

    # print(elf)


print(part1())
print(part2())
