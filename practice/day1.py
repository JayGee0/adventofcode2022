file = open("day1.txt", "r")
contents = file.readlines()

sum = 0
for i in range(len(contents) - 1):
    a = int(contents[i])
    b = int(contents[i+1])
    if a < b:
        sum += 1

print(sum)