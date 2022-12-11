import math

file = open("day9/input.txt", "r")
contents = file.readlines()


def part1():
    visited = []
    head_pos = (0, 0)
    tail_pos = (0, 0)

    for i in range(len(contents)):
        line = contents[i].strip().split()
        direction = line[0]
        amount = int(line[1])
        print(direction, amount)

        for j in range(amount):
            h_x = head_pos[0]
            h_y = head_pos[1]

            if direction == "U":
                head_pos = (h_x, h_y + 1)
            elif direction == "R":
                head_pos = (h_x + 1, h_y)
            elif direction == "D":
                head_pos = (h_x, h_y - 1)
            else:
                head_pos = (h_x - 1, h_y)

            h_x = head_pos[0]
            h_y = head_pos[1]

            near = False
            t_x = tail_pos[0]
            t_y = tail_pos[1]

            for dy in range(-1, 2):
                for dx in range(-1, 2):
                    if h_x - t_x + dx == 0 and h_y - t_y + dy == 0:
                        near = True

            if not near:
                if t_x == h_x or t_y == h_y:
                    if direction == "U":
                        tail_pos = (t_x, t_y + 1)
                    elif direction == "R":
                        tail_pos = (t_x + 1, t_y)
                    elif direction == "D":
                        tail_pos = (t_x, t_y - 1)
                    else:
                        tail_pos = (t_x - 1, t_y)
                else:
                    if direction == "U":
                        tail_pos = (h_x, h_y - 1)
                    elif direction == "R":
                        tail_pos = (h_x - 1, h_y)
                    elif direction == "D":
                        tail_pos = (h_x, h_y + 1)
                    else:
                        tail_pos = (h_x + 1, h_y)

            print(tail_pos, head_pos)
            if tail_pos not in visited:
                visited.append(tail_pos)

    print(len(visited))


def part2():
    visited = []
    head_pos = (0, 0)
    tail_pos = [(0, 0)] * 9

    for i in range(len(contents)):
        line = contents[i].strip().split()
        direction = line[0]
        amount = int(line[1])
        print(direction, amount)

        for j in range(amount):
            h_x = head_pos[0]
            h_y = head_pos[1]

            if direction == "U":
                head_pos = (h_x, h_y + 1)
            elif direction == "R":
                head_pos = (h_x + 1, h_y)
            elif direction == "D":
                head_pos = (h_x, h_y - 1)
            else:
                head_pos = (h_x - 1, h_y)

            pos_history = []
            for k in range(len(tail_pos)):
                if k == 0:
                    h_x = head_pos[0]
                    h_y = head_pos[1]
                else:
                    h_x = tail_pos[k - 1][0]
                    h_y = tail_pos[k - 1][1]

                pos_history.append(tail_pos[k])

                near = False
                t_x = tail_pos[k][0]
                t_y = tail_pos[k][1]

                for dy in range(-1, 2):
                    for dx in range(-1, 2):
                        if h_x - t_x + dx == 0 and h_y - t_y + dy == 0:
                            near = True

                if not near:
                    if t_x == h_x or t_y == h_y:
                        if h_y - t_y > 1:
                            tail_pos[k] = (t_x, t_y + 1)
                        elif h_x - t_x > 1:
                            tail_pos[k] = (t_x + 1, t_y)
                        elif t_y - h_y > 1:
                            tail_pos[k] = (t_x, t_y - 1)
                        else:
                            tail_pos[k] = (t_x - 1, t_y)
                    else:
                        if not(abs(h_x - t_x) >= 1 and abs(h_y - t_y) >= 1) or k == 0:
                            if h_y - t_y > 1:
                                tail_pos[k] = (h_x, h_y - 1)
                            elif h_x - t_x > 1:
                                tail_pos[k] = (h_x - 1, h_y)
                            elif t_y - h_y > 1:
                                tail_pos[k] = (h_x, h_y + 1)
                            else:
                                tail_pos[k] = (h_x + 1, h_y)
                        else:
                            print("diagonal")
                            tail_pos[k] = pos_history[-2]

                print(tail_pos)

                if tail_pos[8] not in visited:
                    visited.append(tail_pos[k])

        print(tail_pos, head_pos)

    print(len(visited))


# part1()
part2()
