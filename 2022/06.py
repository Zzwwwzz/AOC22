def p1(data, size):
    for (i, _) in enumerate(data):

        if len(set(data[i:(i+size)])) == size:
            return i + size

def main():
    data = open("i/6.txt").read()
    print(f'Part 1: {p1(data, 4)}')
    print(f'Part 1: {p1(data, 14)}')

main()
