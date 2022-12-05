file = open("day5/input.txt", "r")
contents = file.readlines()

stacks = [[]] * 9
#             [C]         [N] [R]
# [J] [T]     [H]         [P] [L]
# [F] [S] [T] [B]         [M] [D]
# [C] [L] [J] [Z] [S]     [L] [B]
# [N] [Q] [G] [J] [J]     [F] [F] [R]
# [D] [V] [B] [L] [B] [Q] [D] [M] [T]
# [B] [Z] [Z] [T] [V] [S] [V] [S] [D]
# [W] [P] [P] [D] [G] [P] [B] [P] [V]
#  1   2   3   4   5   6   7   8   9


#     [D]
# [N] [C]
# [Z] [M] [P]
#  1   2   3

#
# stacks[0] = [*"ZN"]
# stacks[1] = [*"MCD"]
# stacks[2] = [*"P"]

stacks[0] = [*"WBDNCFJ"]
stacks[1] = [*"PZVQLST"]
stacks[2] = [*"PZBGJT"]
stacks[3] = [*"DTLJZBHC"]
stacks[4] = [*"GVBJS"]
stacks[5] = [*"PSQ"]
stacks[6] = [*"BVDFLMPN"]
stacks[7] = [*"PSMFBDLR"]
stacks[8] = [*"VDTR"]


for i in range(len(contents)):
    line = contents[i].strip()
    if len(line) == 0 or line[0] != "m":
        continue

    line = line.replace("move", " ").replace("from", " ").replace("to", " ")
    movefromto = line.split()

    for j in range(int(movefromto[0])):
        stacks[int(movefromto[2]) - 1].append(stacks[int(movefromto[1]) - 1].pop())

    print(stacks)

string = ""
for i in range(len(stacks)):
    string += stacks[i].pop()

print(string)