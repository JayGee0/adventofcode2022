file = open("day2/input.txt", "r")
contents = file.readlines()


def part1():
    choicetoscore = {"X": 1, "Y": 2, "Z": 3}
    winning = {"A": "Y", "B": "Z", "C": "X"}
    same = {"A": "X", "B": "Y", "C": "Z"}
    total = 0
    for i in range(len(contents)):
        line = contents[i].split()
        total += choicetoscore[line[1]]
        if line[1] == winning[line[0]]:
            total += 6
        if line[1] == same[line[0]]:
            total += 3
        print(total)

    print(total)


def part2():
    resultotscore = {"X": 0, "Y": 3, "Z": 6}
    choicetoscore = {"X": 1, "Y": 2, "Z": 3}

    winning = {"A": "Y", "B": "Z", "C": "X"}
    losing = {"A": "Z", "B": "X", "C": "Y"}
    same = {"A": "X", "B": "Y", "C": "Z"}

    total = 0
    for i in range(len(contents)):
        line = contents[i].split()
        total += resultotscore[line[1]]

        if (line[1] == "X"):
            total += choicetoscore[losing[line[0]]]
        elif (line[1] == "Y"):
            total += choicetoscore[same[line[0]]]
        else:
            total += choicetoscore[winning[line[0]]]

        print(total)

    print(total)


part1()
part2()
