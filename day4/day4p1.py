file = open("day4/input.txt", "r")
contents = file.readlines()

ranges = [[]]
count = 0
for i in range(len(contents)):
    split = contents[i].strip().split(",")
    range1 = split[0].split("-")
    range1 = (int(range1[0]), int(range1[1]))
    range2 = split[1].split("-")
    range2 = (int(range2[0]), int(range2[1]))

    if range1[0] <= range2[0] and range1[1] >= range2[1]:
        count += 1
    elif range2[0] <= range1[0] and range1[1] <= range2[1]:
        count += 1

print(count)
