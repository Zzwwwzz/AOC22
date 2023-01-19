import operator

ops = {
    '+' : operator.add,
    '*' : operator.mul}


def read_file():
    with open("i/11.txt") as f:
        data = f.read().strip().split('\n\n')
    monkeys = []
    for i, monkey in enumerate(data):
        stuff = monkey.split("\n")
        index = i
        items = list(map(int, stuff[1][18:].split(", ")))
        operation = [stuff[2][23:].split(" ")[0], stuff[2][23:].split(" ")[1]]
        test = int(stuff[3][21:])
        trueMon = int(stuff[4][29:])
        falseMon = int(stuff[5][30:])
        monkeys.append([index, items, operation, test, trueMon, falseMon])
        # Monkeys: index, [items], [Op, num], Test, TrueMon, FalseMon
    return monkeys


def monkeyRound(data, monIns, div, part2=False):
    for monkey in data:
        for item in monkey[1]:
            op = ops[monkey[2][0]]
            multiplier = monkey[2][1]

            if multiplier == "old":
                multiplier = item

            if part2:   newItem = op(item, int(multiplier))%div
            else:       newItem = op(item, int(multiplier))//div

            if newItem % monkey[3] == 0:
                data[monkey[4]][1].append(newItem)
            else:
                data[monkey[5]][1].append(newItem)

            monIns[monkey[0]] += 1
        monkey[1] = []

    return data, monIns

def first(data):
    monIns = [0]*len(data)
    for _ in range(20):
        data, monIns = monkeyRound(data, monIns, 3)

    monIns.sort()
    print(f'{monIns[-1]*monIns[-2]}')


def second(data):
    divisor = 1
    for i in data:
        divisor *= int(i[3])

    monIns = [0]*len(data)  
    for _ in range(10000):
        data, monIns = monkeyRound(data, monIns, divisor, True)

    monIns.sort()
    print(f'{monIns[-1]*monIns[-2]}')


def main():
    data = read_file()
    first(data.copy()) #99852
    data = read_file()
    second(data) #25935263541


main()