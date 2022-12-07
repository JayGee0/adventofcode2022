file = open("day3/input.txt", "r")
contents = file.readlines()


def part1():
    score = 0
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphabetmapper = {}
    for i in range(len(alphabet)):
        alphabetmapper[alphabet[i]] = i + 1
    for i in range(len(contents)):
        contents[i] = contents[i].strip()
        firstPart = contents[i][0:(len(contents[i]) // 2)]
        secondPart = contents[i][len(contents[i]) // 2:]
        print(firstPart)
        print(secondPart)

        found = ""
        for j in range(len(firstPart)):
            for k in range(len(secondPart)):
                if firstPart[j] == secondPart[k] and not (secondPart[k] in found):
                    found += firstPart[j]

        for j in range(len(found)):
            print(alphabetmapper[found[j]], found[j])
            score += alphabetmapper[found[j]]

    print(score)


def part2():
    score = 0
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphabetmapper = {}
    for i in range(len(alphabet)):
        alphabetmapper[alphabet[i]] = i + 1

    for i in range(0, len(contents) - 2, 3):
        a = contents[i].strip()
        b = contents[i + 1].strip()
        c = contents[i + 2].strip()

        found = ""
        for j in range(len(a)):
            for k in range(len(b)):
                for l in range(len(c)):
                    if a[j] == b[k] == c[l] and not (c[l] in found):
                        found += a[j]

        for j in range(len(found)):
            print(i)
            print(alphabetmapper[found[j]], found[j])
            score += alphabetmapper[found[j]]

    print(score)


part1()
part2()