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


def blocking(checkY, checkX, sensors, beacons):
    for i in range(len(sensors)):
        s = sensors[i]
        b = beacons[i]
        dist = abs(b[0] - s[0]) + abs(b[1] - s[1])
        if abs(checkY - s[1]) + abs(checkX - s[0]) <= dist:
            return False
    return True

def part2():
    sensors = []
    beacons = []
    dists = []
    for i in range(len(contents)):
        line = contents[i].strip()

        # Use a regular expression to capture the x and y values for each pair
        matches = re.findall(r"x=(-?\d+), y=(-?\d+)", line)
        sensor = (int(matches[0][0]), int(matches[0][1]))
        beacon = (int(matches[1][0]), int(matches[1][1]))
        sensors.append(sensor)
        beacons.append(beacon)
        dists.append(abs(beacon[0] - sensor[0]) + abs(beacon[1] - sensor[1]))

    print(sensors)
    print(beacons)

    check_min = 0
    check_max = 4000000

    perimeter = set()
    for checkY in range(check_min, check_max + 1):
        print("Checking y = ", checkY)
        for i in range(len(sensors)):
            s = sensors[i]
            r = dists[i]

            dist_check = abs(checkY - s[1])
            if dist_check > r:
                continue
            diff_x = abs(r - abs(checkY - s[1])) + 1
            # print(s, b, r, abs(checkY - s[1]))
            if diff_x == 0:
                continue
            for x in range(-diff_x, diff_x+1, diff_x*2):
                # print(s, b, r, diff_x, (s[0] - diff_x-1, checkY), (s[0] + diff_x+1, checkY))

                if not check_min <= x + s[0] <= check_max:
                    continue

                if abs(checkY - s[1]) + abs(x) > r and blocking(checkY, x + s[0], sensors, beacons):
                    perimeter.add((x + s[0], checkY))
                    print(perimeter)
                    total = (x + s[0]) * 4000000 + checkY
                    print(total)
                    quit()


part2()