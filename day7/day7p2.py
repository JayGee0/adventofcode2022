file = open("day7/input.txt", "r")
contents = file.readlines()

path = []
paths = []
dc = {}
for i in range(len(contents)):
    line = contents[i].strip().split(" ")
    if line[0] == "$":
        if line[1] == "cd":
            if line[2] == "..":
                path.pop()
                paths.pop()
            else:
                path.append(line[2])
                paths.append(path.copy())
                dc[str(path)] = 0

    else:
        if line[0] != "dir":
            # dc[str(path)] += int(line[0])
            # print(paths)
            for p in paths:
                dc.update({str(p): dc[str(p)] + int(line[0])})

needed = 30000000 - (70000000 - dc["['/']"])

smallest = dc["['/']"]

for v in dc.keys():
    if needed <= dc[v] < smallest:
        smallest = dc[v]

print(smallest)
