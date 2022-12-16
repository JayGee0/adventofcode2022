file = open("day14/input.txt", "r")
contents = file.readlines()

def part1():
    blocked = set()
    maxY = 0
    for i in range(len(contents)):
        line = contents[i].strip().split(" -> ")
        points = []
        for li in line:
            l = li.split(",")
            x = int(l[0])
            y = int(l[1])

            loc = [x, y]
            points.append(loc)
        for p in range(len(points) - 1):
            p1 = points[p].copy()
            p2 = points[p + 1].copy()

            while p1[0] != p2[0]:
                blocked.add((p1[0], p1[1]))

                if p1[0] > p2[0]:
                    p1[0] -= 1
                else:
                    p1[0] += 1

                blocked.add((p1[0], p1[1]))


            while p1[1] != p2[1]:
                blocked.add((p1[0], p1[1]))

                if p1[1] > p2[1]:
                    p1[1] -= 1
                else:
                    p1[1] += 1

                blocked.add((p1[0], p1[1]))

            if p1[1] > maxY:
                maxY = p1[1]

    print(blocked)

    sand = [500, 0]
    sands = []
    while sand[1] < maxY:
        #Fall
        down = (sand[0], sand[1] + 1)
        if down not in blocked:
            sand = down
            continue

        dl = (sand[0] - 1, sand[1] + 1)
        if dl not in blocked:
            sand = dl
            continue

        dr = (sand[0] + 1, sand[1] + 1)
        if dr not in blocked:
            sand = dr
            continue

        blocked.add(sand)
        sands.append(sand)
        sand = [500, 0]


    for i in range(10):
        row = []
        for j in range(20):
            if (j + 490, i) in blocked:
                if (j + 490, i) in sands:
                    row.append("o")
                else:
                    row.append("#")
            else:
                row.append(".")
        print(row)

    print(len(sands))

def part2():
    blocked = set()
    maxY = 0
    for i in range(len(contents)):
        line = contents[i].strip().split(" -> ")
        points = []
        for li in line:
            l = li.split(",")
            x = int(l[0])
            y = int(l[1])

            loc = [x, y]
            points.append(loc)
        for p in range(len(points) - 1):
            p1 = points[p].copy()
            p2 = points[p + 1].copy()

            while p1[0] != p2[0]:
                blocked.add((p1[0], p1[1]))

                if p1[0] > p2[0]:
                    p1[0] -= 1
                else:
                    p1[0] += 1

                blocked.add((p1[0], p1[1]))


            while p1[1] != p2[1]:
                blocked.add((p1[0], p1[1]))

                if p1[1] > p2[1]:
                    p1[1] -= 1
                else:
                    p1[1] += 1

                blocked.add((p1[0], p1[1]))

            if p1[1] > maxY:
                maxY = p1[1]

    print(blocked)

    sand = (500, 0)
    sands = []
    while True:
        #Fall
        down = (sand[0], sand[1] + 1)

        if down not in blocked and down[1] != maxY + 2:
            sand = down
            continue

        dl = (sand[0] - 1, sand[1] + 1)
        if dl not in blocked and dl[1] != maxY + 2:
            sand = dl
            continue

        dr = (sand[0] + 1, sand[1] + 1)
        if dr not in blocked and dr[1] != maxY + 2:
            sand = dr
            continue

        blocked.add(sand)
        sands.append(sand)
        if sand == (500, 0):
            break

        # for i in range(15):
        #     row = []
        #     for j in range(20):
        #         if (j + 490, i) in blocked:
        #             if (j + 490, i) in sands:
        #                 row.append("o")
        #             else:
        #                 row.append("#")
        #         else:
        #             row.append(".")
        #     print(row)

        sand = (500, 0)


    for i in range(15):
        row = []
        for j in range(20):
            if (j + 490, i) in blocked:
                if (j + 490, i) in sands:
                    row.append("o")
                else:
                    row.append("#")
            else:
                row.append(".")
        print(row)

    print(len(sands))

part2()