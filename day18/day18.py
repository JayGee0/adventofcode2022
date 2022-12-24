file = open("day18/input.txt", "r")
contents = file.readlines()


def part1():
    print("Part1")
    cubes = set()
    for line in contents:
        x, y, z = line.split(",")
        cubes.add((int(x), int(y), int(z)))

    covered = 0

    for ci, cube in enumerate(cubes):
        x, y, z = cube
        print(ci, len(cubes))
        for i in range(ci, len(cubes)):
            x2, y2, z2 = list(cubes)[i]
            if abs(x - x2) == 1 and y == y2 and z == z2:
                covered += 2
            if abs(y - y2) == 1 and x == x2 and z == z2:
                covered += 2
            if abs(z - z2) == 1 and y == y2 and x == x2:
                covered += 2

    print(len(cubes) * 6 - covered)


def part2():
    print("Part2")
    cubes = set()
    for line in contents:
        x, y, z = line.split(",")
        cubes.add((int(x), int(y), int(z)))

    covered = 0

    for ci, cube in enumerate(cubes):
        x, y, z = cube
        print(ci, len(cubes))
        for i in range(ci, len(cubes)):
            x2, y2, z2 = list(cubes)[i]
            if abs(x - x2) == 1 and y == y2 and z == z2:
                covered += 2
            if abs(y - y2) == 1 and x == x2 and z == z2:
                covered += 2
            if abs(z - z2) == 1 and y == y2 and x == x2:
                covered += 2

    print(len(cubes) * 6 - covered)


part1()