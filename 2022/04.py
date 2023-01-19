def readFile():
    with open("i/4.txt") as file:
        data = [line.strip().split(",") for line in file.read().splitlines()]
    return data

def p1(data):
    p1, p2 = 0, 0
    for pair in data:
        a = [int(i) for i in pair[0].split("-")]
        b = [int(i) for i in pair[1].split("-")]
        if (a[0] <= b[0] and b[1] <= a[1]):
            p1 += 1
        elif (b[0] <= a[0] and a[1] <= b[1]):
            p1 += 1
        if (b[0] <= a[1] and b[1] >= a[1]):
            p2 += 1
        elif (a[0] <= b[1] and a[1] >= b[1]):
            p2 += 1
    return p1, p2


def main():
    data = readFile()

    print(f'Part 1: {p1(data)[0]}')
    print(f'Part 2: {p1(data)[1]}')

main()
