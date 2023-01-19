from operator import add, mul, sub, floordiv

operators = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": floordiv
}

def sign(n):
    if n > 0:
        return 1
    elif n < 0:
        return -1
    else:
        return 0


def readFile():
    data = open("i/21.txt").read().split("\n")
    monkeys = dict()
    for line in data:
        m, *ops = line.split()
        m = m[:-1]
        if len(ops) == 1:
            monkeys[m] = int(ops[0])
        else:
            monkeys[m] = (operators[ops[1]], ops[0], ops[2])
    return monkeys


def p1(monkeys, m='root'):
    if type(monkeys[m]) is int:
        return monkeys[m]
    else:
        op, l, r = monkeys[m]
        return op(p1(monkeys, l), p1(monkeys, r))


def p2(monkeys):
    _, l, r = monkeys['root']
    monkeys['root'] = (sub, l, r)
    root_value = p1(monkeys)
    initial_sign = sign(root_value)
    space = (0, 99999999999999)
    while root_value:
        mid = sum(space) // 2
        monkeys['humn'] = mid
        root_value = p1(monkeys)
        if sign(root_value) == initial_sign:
            space = (mid+1, space[1])
        else:
            space = (space[0], mid)
    return monkeys['humn']

def main():
    monkeys = readFile()

    print(f'Part 1: {p1(monkeys)}')
    print(f'Part 2: {p2(monkeys)}')


main()
