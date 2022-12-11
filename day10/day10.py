file = open("day10/input.txt", "r")
contents = file.readlines()

def part1():

    #instruction_buffer = {}
    X = 1
    clock_counter = 0
    signal = 0
    for i in range(len(contents)):
        line = contents[i].strip().split()
        # for b in instruction_buffer.keys():
        #     if i == b:
        #         X += instruction_buffer[b]

        if line[0] == "addx":
            clock_counter += 1
            if (clock_counter - 20) % 40 == 0 and clock_counter <= 220:
                signal += clock_counter * X
                print(clock_counter, X, clock_counter * X)

            clock_counter += 1
            if (clock_counter - 20) % 40 == 0 and clock_counter <= 220:
                signal += clock_counter * X
                print(clock_counter, X, clock_counter * X)

            X += int(line[1])



        else:
            clock_counter += 1

            if (clock_counter - 20) % 40 == 0 and clock_counter <= 220:
                signal += clock_counter * X
                print(clock_counter, X, clock_counter * X)

    print(signal)
    print("part1")


#instruction_buffer = {}
X = 1
clock_counter = 0
signal = 0
screen = []

def cycle():
    global clock_counter, signal, row_counter, row_string
    clock_counter += 1
    if clock_counter == 41 or clock_counter == 81 or clock_counter == 121 or clock_counter == 161 or clock_counter == 201:
        row_counter += 1
        screen.append(row_string)
        row_string = ""
    draw_screen()
    print(row_string)
    print()


row_counter = 0
row_string = ""

def draw_screen():
    global row_string
    print(clock_counter, X)
    sprite_pos = [X - 1, X, X + 1]

    col = (clock_counter-1) % 40
    print(col)
    if col in sprite_pos:
        row_string += "█"
    else:
        row_string += " "



for i in range(len(contents)):
    line = contents[i].strip().split()
    # for b in instruction_buffer.keys():
    #     if i == b:
    #         X += instruction_buffer[b]

    if line[0] == "addx":
        cycle()
        cycle()
        X += int(line[1])
    else:
        cycle()

screen.append(row_string)
print(signal)
[print(row) for row in screen]
print("part2")


#part1()
