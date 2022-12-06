file = open("day6/input.txt", "r")
contents = file.readlines()

markers = []
code = [*contents[0]]

for i in range(len(code) - 14):
    total = []
    for j in range(14):
        if code[i + j] in total:
            break
        else:
            total.append(code[i + j])
    if len(total) == 14:
        print(i + 14)
        break
