
def priority(c):
    if c.islower():
        return ord(c) - ord("a") + 1
    else:
        return ord(c) - ord("A") + 27

def readData():
    with open("i/3.txt") as f:
        lines = f.read().split()
    return lines

def p1(lines):
    p1 = 0
    for line in lines:
        a, b = set(line[:len(line)//2]), set(line[len(line)//2:])
        c = next(iter(a.intersection(b)))
        p1 += priority(c)

    return p1

def p2(lines):
    p2, i = 0, 0
    for i in range(0, len(lines), 3):
        group = lines[i: i + 3]
        commonItem = next(iter(set(group[0]).intersection(set(group[1])).intersection(set(group[2]))))
        p2 += priority(commonItem)

    return p2


def main():
    lines = readData()
    print(f'Part 1: {p1(lines)}')
    print(f'Part 2: {p2(lines)}')


main()