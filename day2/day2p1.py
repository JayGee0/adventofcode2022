file = open("day2/input.txt", "r")
contents = file.readlines()

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