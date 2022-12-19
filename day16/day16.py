import networkx as nx
import re
from collections import deque as de

file = open("day16/input.txt", "r")
contents = file.readlines()

def part1():
    connections = {}
    flows = {}
    for i in range(len(contents)):
        s = contents[i].strip()
        c = re.findall(r'\b[A-Z]{2}\b', s)
        f = int(re.findall(r'\d+', s)[0])
        connected = []
        for j in range(1, len(c)):
            connected.append(c[j])
        connections[c[0]] = connected
        flows[c[0]] = f

    # print(connections)
    # print(flows)

    #https://www.youtube.com/watch?v=bLMj50cpOug
    # Figuring out the distance between each of the flowing nodes using bfs
    dists = {}

    for valve in connections.keys():
        # if they don't flow, then they don't go
        if valve != "AA" and not flows[valve]:
            continue

        # Connected nodes and their distances
        dists[valve] = {}
        visited = {valve}
        # distance, node
        q = de([(0, valve)])

        while q:
            distance, node = q.popleft()
            neighbors = connections[node]
            for n in neighbors:
                if n in visited:
                    continue
                visited.add(n)
                if flows[n]:
                    dists[valve][n] = distance + 1
                q.append((distance + 1, n))

    print(dists)
    [print(d) for d in dists]
    nonempty = set(dists.keys())
    nonempty.remove("AA")
    print(nonempty)
    # DFS and Bitmask approach
    cache = {}

    indices = {}
    for index, element in enumerate(nonempty):
        indices[element] = index
    print(indices)

    def dfs(minutes, valve, bitmask):
        if (minutes, valve, bitmask) in cache:
            return cache[(minutes, valve, bitmask)]
        max_flow = 0
        for n in dists[valve]:
            # Bitify the node
            bit = 1 << indices[n]
            # If bit is on in the bitmask then badoom
            # If valve is open already
            if bitmask & bit:
                continue

            # Checking the remaining time if I were to traverse the path to get to the
            # next flow-full node
            remaining_time = minutes - dists[valve][n] - 1

            # If the remaining time after traversing is less than 0 (impossible) then don't
            if remaining_time <= 0:
                continue

            max_flow = max(max_flow, dfs(remaining_time, n, bitmask | bit) + flows[n] * remaining_time)

        cache[(minutes, valve, bitmask)] = max_flow
        # print(minutes, valve, max_flow)
        return max_flow

    print(dfs(30, "AA", 0))

def part2():
    print("Part2")
    connections = {}
    flows = {}
    for i in range(len(contents)):
        s = contents[i].strip()
        c = re.findall(r'\b[A-Z]{2}\b', s)
        f = int(re.findall(r'\d+', s)[0])
        connected = []
        for j in range(1, len(c)):
            connected.append(c[j])
        connections[c[0]] = connected
        flows[c[0]] = f

    # print(connections)
    # print(flows)

    #https://www.youtube.com/watch?v=bLMj50cpOug
    # Figuring out the distance between each of the flowing nodes using bfs
    dists = {}

    for valve in connections.keys():
        # if they don't flow, then they don't go
        if valve != "AA" and not flows[valve]:
            continue

        # Connected nodes and their distances
        dists[valve] = {}
        visited = {valve}
        # distance, node
        q = de([(0, valve)])

        while q:
            distance, node = q.popleft()
            neighbors = connections[node]
            for n in neighbors:
                if n in visited:
                    continue
                visited.add(n)
                if flows[n]:
                    dists[valve][n] = distance + 1
                q.append((distance + 1, n))

    print(dists)
    [print(d) for d in dists]
    nonempty = set(dists.keys())
    nonempty.remove("AA")
    print(nonempty)
    # DFS and Bitmask approach
    cache = {}

    indices = {}
    for index, element in enumerate(nonempty):
        indices[element] = index
    print(indices)

    def dfs(minutes, valve, bitmask):
        if (minutes, valve, bitmask) in cache:
            return cache[(minutes, valve, bitmask)]
        max_flow = 0
        for n in dists[valve]:
            # Bitify the node
            bit = 1 << indices[n]
            # If bit is on in the bitmask then badoom
            # If valve is open already
            if bitmask & bit:
                continue

            # Checking the remaining time if I were to traverse the path to get to the
            # next flow-full node
            remaining_time = minutes - dists[valve][n] - 1

            # If the remaining time after traversing is less than 0 (impossible) then don't
            if remaining_time <= 0:
                continue

            max_flow = max(max_flow, dfs(remaining_time, n, bitmask | bit) + flows[n] * remaining_time)

        cache[(minutes, valve, bitmask)] = max_flow
        # print(minutes, valve, max_flow)
        return max_flow

    # Spoofing the bitmask to say that one half of the valves are already opened
    # So that the elephant can go for the other ones

    # All valves currently opened
    max_bit = (1 << (len(nonempty))) - 1
    # e.g. 111111

    # Iterating through every possible solution of bitmask
    # e.g.
    # 10010001 <-- i, the one we will check with
    # 01101110 <-- The complement [elephant checks], can be gotten from XOR-ing with the max_bit

    max_flow = 0
    for i in range(max_bit + 1):

        max_flow = max(max_flow, (dfs(26, "AA", i) + dfs(26, "AA", max_bit ^ i)))

    print(max_flow)

part1()
part2()