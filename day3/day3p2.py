file = open("day3/input.txt", "r")
contents = file.readlines()

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
