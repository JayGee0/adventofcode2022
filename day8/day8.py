file = open("day8/input.txt", "r")
contents = file.readlines()


def check_valid(grid, index):
    y = index[1]
    x = index[0]

    if y < 0 or x < 0:
        return False

    if y >= len(grid) or x >= len(grid[0]):
        return False

    return True


def get_valid_indices(grid, index):
    x = index[1]
    y = index[0]

    up = []
    for i in range(1, y + 1):
        if check_valid(grid, (y - i, x)):
            up.append((y - i, x))

    down = []
    for i in range(1, len(grid) - y + 1):
        if check_valid(grid, (y + i, x)):
            down.append((y + i, x))

    right = []
    for i in range(1, x + 1):
        if check_valid(grid, (y, x - i)):
            right.append((y, x - i))

    left = []
    for i in range(1, len(grid[0]) - x + 1):
        if check_valid(grid, (y, x + i)):
            left.append((y, x + i))

    return (up, down, left, right)


def part1():
    vis_count = 0
    grid = []
    for line in contents:
        grid.append([int(i) for i in [*line.strip()]])

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            loc = (i, j)
            if i == 0 or i == len(grid) - 1 or j == 0 or j == len(grid[0]) - 1:
                vis_count += 1
                continue

            near = get_valid_indices(grid, loc)
            # print(loc)
            for dir in near:
                if not any(grid[l[0]][l[1]] >= grid[i][j] for l in dir):
                    vis_count += 1
                    print(near, loc)

                    break

    print(vis_count)


def part2():
    vis_count = 0
    grid = []
    for line in contents:
        grid.append([int(i) for i in [*line.strip()]])

    best_loc = []
    best_score = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            loc = (i, j)
            scenes = get_valid_indices(grid, loc)
            score = 1
            for direction in scenes:
                trees = 0
                for k in direction:
                    trees += 1

                    if grid[k[0]][k[1]] >= grid[i][j]:
                        break

                score *= trees

            if score > best_score:
                best_loc = loc
                best_score = score

    print(best_score)
    print(best_loc)


part1()
part2()
