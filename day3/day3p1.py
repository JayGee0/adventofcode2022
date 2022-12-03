file = open("day3/input.txt", "r")
contents = file.readlines()

score = 0
alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabetmapper = {}
for i in range(len(alphabet)):
    alphabetmapper[alphabet[i]] = i + 1
for i in range(len(contents)):
    contents[i] = contents[i].strip()
    firstPart = contents[i][0:(len(contents[i])//2)]
    secondPart = contents[i][len(contents[i])//2:]
    print(firstPart)
    print(secondPart)

    found = ""
    for j in range(len(firstPart)):
        for k in range(len(secondPart)):
            if firstPart[j] == secondPart[k] and not(secondPart[k] in found):
                found += firstPart[j]

    for j in range(len(found)):
        print(alphabetmapper[found[j]], found[j])
        score += alphabetmapper[found[j]]

print(score)