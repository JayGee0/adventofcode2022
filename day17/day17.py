file = open("day17/input.txt", "r")
contents = file.readlines()

def part1():
    print("Part1")
    #https://www.youtube.com/watch?v=w9Sk7lvyGZI&list=PLnNm9syGLD3yf-YW-a5XNh1CJN07xr0Kz&index=17

    # Storing the rock structures as said in the day17 page
    # as complex numbers
    rocks = [
        [0, 1, 2, 3],
        [1, 1j, 1 + 1j, 2 + 1j, 1 + 2j],
        [0, 1, 2, 2 + 1j, 2 + 2j],
        [0, 1j, 2j, 3j],
        [0, 1, 1j, 1 + 1j],
    ]

    jets = [1 if x == ">" else -1 for x in contents[0].strip()]

    # Covering the whole horizontal
    solid = {x - 1j for x in range(7)}
    height = 0

    # Storing the current rock count and what rock we are currently on
    rock_count = 0
    rock_index = 0

    # Transforming every coordinate of the rock by (2, 3)
    current_rock = {x + 2 + (height + 3) * 1j for x in rocks[rock_index]}

    iterations = 2022

    while rock_count < iterations:
        for jet in jets:
            moved = {x + jet for x in current_rock}
            if all(0 <= x.real < 7 for x in moved) and not (moved & solid):
                current_rock = moved.copy()

            moved = {x - 1j for x in current_rock}
            if moved & solid:
                solid |= current_rock
                rock_count += 1
                height = max(x.imag for x in solid) + 1
                if rock_count >= iterations:
                    break
                rock_index = rock_count % 5
                current_rock = {x + 2 + (height + 3) * 1j for x in rocks[rock_index]}
            else:
                current_rock = moved.copy()

    print(int(height))
def part2():
    print("Part2")

    #https://www.youtube.com/watch?v=w9Sk7lvyGZI&list=PLnNm9syGLD3yf-YW-a5XNh1CJN07xr0Kz&index=17

    # Storing the rock structures as said in the day17 page
    # as complex numbers
    rocks = [
        [0, 1, 2, 3],
        [1, 1j, 1 + 1j, 2 + 1j, 1 + 2j],
        [0, 1, 2, 2 + 1j, 2 + 2j],
        [0, 1j, 2j, 3j],
        [0, 1, 1j, 1 + 1j],
    ]

    jets = [1 if x == ">" else -1 for x in contents[0].strip()]

    # Covering the whole horizontal
    solid = {x - 1j for x in range(7)}
    height = 0

    # Storing the current rock count and what rock we are currently on
    rock_count = 0
    rock_index = 0

    # Transforming every coordinate of the rock by (2, 3)
    current_rock = {x + 2 + (height + 3) * 1j for x in rocks[rock_index]}

    iterations = 1000000000000

    seen = {}

    def peak():
        upper_contents = [-20] * 7

        for x in solid:
            real = int(x.real)
            imaginary = int(x.imag)

            # Get the top-most block of each column
            upper_contents[real] = max(upper_contents[real], imaginary)

            top = max(upper_contents)

        return tuple(x - top for x in upper_contents)

    old_height = 0
    increments = []
    while rock_count < iterations:
        for ji, jet in enumerate(jets):
            moved = {x + jet for x in current_rock}
            if all(0 <= x.real < 7 for x in moved) and not (moved & solid):
                current_rock = moved.copy()

            moved = {x - 1j for x in current_rock}
            if moved & solid:
                solid |= current_rock
                rock_count += 1
                old_height = height
                height = max(x.imag for x in solid) + 1
                increments.append(int(height - old_height))
                if rock_count >= iterations:
                    break
                rock_index = rock_count % 5
                current_rock = {x + 2 + (height + 3) * 1j for x in rocks[rock_index]}
                key = (ji, rock_index, peak())
                if key in seen:
                    last_rock_count, last_height = seen[key]
                    remainder = iterations - rock_count
                    repetitions = remainder // (rock_count - last_rock_count)

                    # Skip ahead a few repetitions
                    offset = repetitions * (height - last_height)
                    rock_count += repetitions * (rock_count - last_rock_count)

                    seen = {}
                seen[key] = (rock_count, height)
            else:
                current_rock = moved.copy()
        print(rock_count)

    print(int(height + offset))


part1()
part2()