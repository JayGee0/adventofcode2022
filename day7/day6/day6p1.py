file = open("day6/input.txt", "r")
contents = file.readlines()

markers = []
code = [*contents[0]]

for i in range(len(code) - 4):
    total = []
    for j in range(4):
        if code[i + j] in total:
            break
        else:
            total.append(code[i + j])
    if len(total) == 4:
        print(i + 4)
        break
