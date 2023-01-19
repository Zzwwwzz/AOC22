from collections import defaultdict

def readFile():
    occupied = set()
    for y, row in enumerate(open('i/23.txt').read().strip().splitlines()):
        for x, col in enumerate(row):
            if col == '#':
                occupied.add(x+y*1j)
    return occupied

def solve(occupied):

    directions = [((-1j, 1-1j, -1-1j), -1j), # N
            ((1j, 1+1j, -1+1j), 1j), # S
            ((-1, -1+1j, -1-1j), -1), # W
            ((1, 1+1j, 1-1j), 1)] # E

    neighbours = set([d for n, dir in directions for d in n])

    moves = 1
    rounds = 0
    while moves != 0:
        if rounds == 10:
            x = [z.real for z in occupied]
            y = [z.imag for z in occupied]
            p1 = (max(x) - min(x) + 1) * (max(y) - min(y) + 1) - len(occupied)
        next = defaultdict(lambda:[])
        for elf in occupied:
            if all([(elf+n) not in occupied for n in neighbours]):
                continue
            for adj, dir in directions:
                if all([(elf+p) not in occupied for p in adj]):
                    next[elf+dir].append(elf)
                    break
        moves = 0
        for candidate, elf in next.items():
            if len(elf) == 1:
                occupied.remove(elf[0])
                occupied.add(candidate)
                moves += 1
        directions.append(directions.pop(0))
        rounds += 1

    return int(p1), rounds

def main():
    occupied = readFile()
    p1, p2 = solve(occupied)
    print(f'Part 1: {p1}')
    print(f'Part 2: {p2}')


main()