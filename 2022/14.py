from collections import defaultdict

def readFile():
    with open("i/14.txt", "r") as file:
            data = [[(int((z := y.split(","))[0]), int(z[1])) for y in x.split(" -> ")] for x in file.read().splitlines()]
    return data

def fall(grid, current, queue, end, p1=None, grains=0):
    while True:
        x,y = current
        (e, nxt) = next(((e, z - 1) for e, z in enumerate(grid[x]) if z > y))
        if x - 1 in grid and nxt + 1 in grid[x - 1]:
            if x + 1 in grid and nxt + 1 in grid[x + 1]:
                grid[x].insert(e, nxt)
                grains += 1
                if not p1 and nxt == end - 1:
                    p1 = grains - 1
                elif nxt == 0:
                    return p1, grains
                c, current = next((((i, (x, y))) for i, (x, y) in enumerate(queue) if x in grid and y not in grid[x]))
                queue = queue[c:]
                continue
            current = (x + 1, nxt + 1)
        else:
            current = (x - 1, nxt + 1)
        queue.insert(0, (x, nxt))


def simulate(data):
    grid = defaultdict(list)
    for rock in data:
        current = rock[0]
        for nxt in rock[1:]:
            for y in range(min(current[1], nxt[1]), max(current[1], nxt[1]) + 1):
                for x in range(min(current[0], nxt[0]), max(current[0], nxt[0]) + 1):
                    grid[x].append(y)
                    current = nxt
    mx = max(sum(grid.values(), [])) + 2
    grid = defaultdict(lambda: [mx], grid)
    for x in range(500 - mx - 1, 500 + mx + 2):
        grid[x].append(mx)
    p1, p2 = fall({k : sorted(set(v)) for k, v in grid.items()}, (500, 0), [(500, 0)], mx)
    return p1, p2

def main():
        data = readFile()
        p1, p2 = simulate(data)
       
        print(f'Part 1: {p1}')
        print(f'Part 1: {p2}')

main()

