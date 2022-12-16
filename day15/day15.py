import re

file = open("day15/input.txt", "r")
contents = file.readlines()

def part1():
    sensors = []
    beacons = []
    for i in range(len(contents)):
        line = contents[i].strip()

        # Use a regular expression to capture the x and y values for each pair
        matches = re.findall(r"x=(-?\d+), y=(-?\d+)", line)
        sensor = (int(matches[0][0]), int(matches[0][1]))
        beacon = (int(matches[1][0]), int(matches[1][1]))
        sensors.append(sensor)
        beacons.append(beacon)

    print(sensors)
    print(beacons)

    blocked = set()
    checkY = 2000000
    for i in range(len(sensors)):
        s = sensors[i]
        b = beacons[i]
        dist = abs(b[0] - s[0]) + abs(b[1] - s[1])
        dist_check = abs(checkY - s[1])
        print("Checking for ", s, dist, dist_check)
        if dist_check <= dist:
            for x in range(-dist, dist+1):
                if abs(dist_check) + abs(x) <= dist:
                    blocked.add((x + s[0], checkY))

    print(len(blocked)-1)


def blocking(checkY, sensors, beacons):
    blocked = set()
    for i in range(len(sensors)):
        s = sensors[i]
        b = beacons[i]
        dist = abs(b[0] - s[0]) + abs(b[1] - s[1])
        dist_check = abs(checkY - s[1])
        if dist_check <= dist:
            #print("Checking for ", s, dist, dist_check)

            if s[0] - dist < 0:
                min_check = 0
            else:
                min_check = -dist

            if s[0] + dist > 4000000:
                max_check = 4000000
            else:
                max_check = dist

            for x in range(-min_check, max_check + 1):
                if abs(dist_check) + abs(x) <= dist:
                    blocked.add((x + s[0], checkY))

    return blocked

def part2():
    sensors = []
    beacons = []
    for i in range(len(contents)):
        line = contents[i].strip()

        # Use a regular expression to capture the x and y values for each pair
        matches = re.findall(r"x=(-?\d+), y=(-?\d+)", line)
        sensor = (int(matches[0][0]), int(matches[0][1]))
        beacon = (int(matches[1][0]), int(matches[1][1]))
        sensors.append(sensor)
        beacons.append(beacon)

    print(sensors)
    print(beacons)

    blocked = set()
    check_min = 0
    check_max = 4000000
    for i in range(check_min, check_max + 1):
        print("Checking y = ", i)
        blocked.update(blocking(i, sensors, beacons))
        print(blocked)

    print(len(blocked)-1)
    for i in range(check_max + 1):
        for j in range(check_max + 1):
            if (i, j) not in blocked:
                print(i, j)
                print(i * 4000000 + j)

part2()