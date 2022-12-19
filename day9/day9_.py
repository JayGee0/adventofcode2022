import math

file = open("day9/input.txt", "r")
contents = file.readlines()


def part1():
    visited = set([(0, 0)])

    head = [0, 0]
    tail = [0, 0]

    for line in contents:
        direction, amount = line.split()
        amount = int(amount)

        for _ in range(amount):
            dx = 1 if direction == "R" else -1 if direction == "L" else 0
            dy = 1 if direction == "U" else -1 if direction == "D" else 0

            head[0] += dx
            head[1] += dy

            _x = head[0] - tail[0]
            _y = head[1] - tail[1]

            if abs(_x) > 1 or abs(_y) > 1:
                if _x == 0:
                    tail[1] += _y // 2
                elif _y == 0:
                    tail[0] += _x // 2
                else:
                    # Move diagonally
                    tail[0] += 1 if _x > 0 else -1
                    tail[1] += 1 if _y > 0 else -1

            visited.add(tuple(tail))

    print(len(visited))


def part2():
    visited = set([(0, 0)])

    head = [0, 0]
    tail = [0, 0]

    # Have to do it like this because [] * x will make x copies of the reference []
    rope = [[0, 0] for i in range(10)]


    for line in contents:
        direction, amount = line.split()
        amount = int(amount)

        for _ in range(amount):
            dx = 1 if direction == "R" else -1 if direction == "L" else 0
            dy = 1 if direction == "U" else -1 if direction == "D" else 0

            rope[0][0] += dx
            rope[0][1] += dy

            for i in range(9):
                head = rope[i]
                tail = rope[i + 1]
                _x = head[0] - tail[0]
                _y = head[1] - tail[1]

                if abs(_x) > 1 or abs(_y) > 1:
                    if _x == 0:
                        tail[1] += _y // 2
                    elif _y == 0:
                        tail[0] += _x // 2
                    else:
                        # Move diagonally
                        tail[0] += 1 if _x > 0 else -1
                        tail[1] += 1 if _y > 0 else -1

            visited.add(tuple(rope[-1]))

    print(len(visited))


part1()
part2()
