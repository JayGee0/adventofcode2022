from math import gcd

file = open("day11/input.txt", "r")
contents = file.readlines()


class Monkey:
    items = []
    operation = []
    test_modulus = 0
    true_monkey = 0
    false_monkey = 0
    inspect_count = 0

    def __init__(self, items, operation, test_modulus, true_monkey, false_monkey):
        self.items = items.copy()
        self.operation = operation.copy()
        self.test_modulus = test_modulus
        self.true_monkey = true_monkey
        self.false_monkey = false_monkey

    def __repr__(self):
        return "Monkey inspected " + str(self.inspect_count) + " times"


def part1():
    monkeys = []
    for i in range(0, len(contents), 7):
        items_string = contents[i + 1].strip().replace(",", "").replace("Starting items: ", "").split()
        items = []
        for it in items_string:
            items.append(int(it))
        print(items)

        operation_string = contents[i + 2].strip().replace("Operation: new = old ", "").split()
        print(operation_string)

        test_modulus = int(contents[i+3].strip().replace("Test: divisible by ", ""))
        print(test_modulus)

        true_monkey = int(contents[i+4].strip().replace("If true: throw to monkey ", ""))
        false_monkey = int(contents[i+5].strip().replace("If false: throw to monkey ", ""))

        print(true_monkey)
        print(false_monkey)

        monk = Monkey(items, operation_string, test_modulus, true_monkey, false_monkey)
        monkeys.append(monk)

    print(monkeys)
    [print("Monkey ", i, ": ", monkeys[i]) for i in range(len(monkeys))]

    for j in range(20):
        for i in range(len(monkeys)):
            m = monkeys[i]
            for it in range(len(m.items)):
                m.inspect_count += 1
                if m.operation[0] == "*":
                    if m.operation[1] == "old":
                        m.items[it] = m.items[it] * m.items[it]
                    else:
                        m.items[it] *= int(m.operation[1])
                else:
                    if m.operation[1] == "old":
                        m.items[it] = m.items[it] + m.items[it]
                    else:
                        m.items[it] += int(m.operation[1])
                m.items[it] //= 3

            it = 0
            while it < len(m.items):
                if m.items[it] % m.test_modulus == 0:
                    monkeys[m.true_monkey].items.append(m.items[it])
                else:
                    monkeys[m.false_monkey].items.append(m.items[it])

                del m.items[it]
                it -= 1
                it += 1

    [print("Monkey ", i, ": ", monkeys[i]) for i in range(len(monkeys))]


def part2():
    monkeys = []
    mods = []
    for i in range(0, len(contents), 7):
        items_string = contents[i + 1].strip().replace(",", "").replace("Starting items: ", "").split()
        items = []
        for it in items_string:
            items.append(int(it))

        operation_string = contents[i + 2].strip().replace("Operation: new = old ", "").split()

        test_modulus = int(contents[i+3].strip().replace("Test: divisible by ", ""))
        mods.append(test_modulus)

        true_monkey = int(contents[i+4].strip().replace("If true: throw to monkey ", ""))
        false_monkey = int(contents[i+5].strip().replace("If false: throw to monkey ", ""))

        monk = Monkey(items, operation_string, test_modulus, true_monkey, false_monkey)
        monkeys.append(monk)

    mods.sort()

    mod = 1
    for i in mods:
        mod = mod * i // gcd(mod, i)
    print(mod)


    print(monkeys)
    [print("Monkey ", i, ": ", monkeys[i]) for i in range(len(monkeys))]

    for j in range(10000):
        for i in range(len(monkeys)):
            m = monkeys[i]
            for it in range(len(m.items)):
                m.inspect_count += 1
                if m.operation[0] == "*":
                    if m.operation[1] == "old":
                        m.items[it] = m.items[it] * m.items[it]
                    else:
                        m.items[it] *= int(m.operation[1])
                else:
                    if m.operation[1] == "old":
                        m.items[it] = m.items[it] + m.items[it]
                    else:
                        m.items[it] += int(m.operation[1])

                m.items[it] %= mod

            it = 0
            while it < len(m.items):
                if m.items[it] % m.test_modulus == 0:
                    monkeys[m.true_monkey].items.append(m.items[it])
                else:
                    monkeys[m.false_monkey].items.append(m.items[it])

                del m.items[it]
                it -= 1
                it += 1

        print("Round " + str(j + 1))
        [print("Monkey ", i, ": ", monkeys[i]) for i in range(len(monkeys))]


part2()
