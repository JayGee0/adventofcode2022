from math import gcd

file = open("day12/input.txt", "r")
contents = file.readlines()


def check_valid(index, grid):
    x = index[1]
    y = index[0]

    if x < 0 or y < 0:
        return False

    if y >= len(grid) or x >= len(grid[0]):
        return False

    return True


def get_neigbours(index, grid):
    x = index[1]
    y = index[0]

    up = (y - 1, x)
    right = (y, x + 1)
    down = (y + 1, x)
    left = (y, x - 1)

    neighbors = {up, right, down, left}
    valid_neighbors = []
    if grid[y][x] == "S":
        place_value = ord("a")
    elif grid[y][x] == "E":
        place_value = ord("z")
    else:
        place_value = ord(grid[y][x])

    for n in neighbors:
        n_x = n[1]
        n_y = n[0]

        if check_valid(n, grid):
            if grid[n_y][n_x] == "S":
                n_value = ord("a")
            elif grid[n_y][n_x] == "E":
                n_value = ord("z")
            else:
                n_value = ord(grid[n_y][n_x])

            if n_value <= place_value or n_value == place_value + 1:
                valid_neighbors.append(n)

    return valid_neighbors


def traverse_path(grid, index, path, route):
    if len(route) >= 1 and len(path) > len(route[0]):
        return

    path.append(index)

    y = index[0]
    x = index[1]
    if grid[y][x] == "E":
        route.append(path.copy())
        route.sort(key=len)
        print("Reached")
        path.pop()
        return

    neighbors = get_neigbours(index, grid)
    for n in neighbors:
        if n not in path:
            traverse_path(grid, n, path, route)

    path.pop()
    return


dynamo = {}


def bfs(grid, start, end):
    if start in dynamo.keys():
        return dynamo[start]
    queue = [[start, [start]]]
    final_path = []
    visited = []
    counter = 0
    while queue:
        visit = queue.pop(0)
        node = visit[0]
        path = visit[1].copy()
        path.append(node)

        if node in visited:
            continue
        if node == end:
            final_path = path.copy()
            break

        neighbours = get_neigbours(node, grid)
        for n in neighbours:
            queue.append([n, path.copy()])

        counter += 1
        visited.append(node)

    #print(len(dynamo.keys()))
    dynamo[start] = len(final_path)
    if len(final_path) == 0:
        return -1
    else:
        return len(final_path)



def part1():
    grid = []
    for i in range(len(contents)):
        line = [*contents[i].strip()]
        grid.append(line)

    start = []
    end = []
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == 'S':
                start = (y, x)

    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == 'E':
                end = (y, x)

    final_path = bfs(grid, start, end)

    print(len(final_path) - 2)
    print(final_path)


# BFS(graph, start_node, end_node):
# frontier = new
# Queue()
# frontier.enqueue(start_node)
# explored = new
# Set()
#
# while frontier is not empty:
#     current_node = frontier.dequeue()
#     if current_node in explored: continue
#     if current_node == end_node: return success
#
#     for neighbor in graph.get_neigbhors(current_node):
#         frontier.enqueue(neighbor)
#     explored.add(current_node)


def part2():
    grid = []
    for i in range(len(contents)):
        line = [*contents[i].strip()]
        grid.append(line)

    starts = []
    end = []
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == 'S' or grid[y][x] == "a":
                starts.append((y, x))

    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == 'E':
                end = (y, x)

    final_path = bfs(grid, starts[0], end)
    print(starts)
    print(final_path)
    for s in starts:
        b = bfs(grid, s, end)
        if b < final_path and b != -1:
            final_path = b
            print(final_path)

    print(final_path - 2)

part1()
part2()
