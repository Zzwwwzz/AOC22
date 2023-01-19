from timeit import default_timer as timer


def read_file():
    data = []

    with open('i/8.txt', 'r') as f:
        for line in f:
            data.append(line.strip())
    return data


def first(data):
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    ans=0
    for i in range(1,len(data)-1):
        for j in range(1,len(str(data[i]))-1):
            for d in dirs:
                x, y = i + d[0], j + d[1]
                while 0 < x < len(data) - 1 and 0 < y < len(data) - 1 and data[i][j] > data[x][y]:
                    x, y = x + d[0], y + d[1]
                if data[i][j] > data[x][y] and (x == 0 or x == len(data) - 1 or y == 0 or y == len(data) - 1):
                    ans += 1
                    break
    print(ans+((len(data)-2)*2)+(len(str(data[i]))*2))


def second(data):
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    ans=0
    for i in range(1,len(data)-1):
        for j in range(1,len(str(data[i]))-1):
            score = 1
            for d in dirs:
                count = 0
                x, y = i + d[0], j + d[1]
                while 0 <= x <= len(data) - 1 and 0 <= y <= len(data) - 1:
                    count += 1
                    if data[i][j] <= data[x][y]:
                        break
                    x, y = x + d[0], y + d[1]
                score *= count
            ans = max(ans, score)
    print(ans)


def main():
    start = timer()
    data = read_file()
    first(data)
    part1 = timer()
    second(data)
    part2 = timer()

    print(f'part 1: {part1-start}\npart 2: {part2-part1}\nBoth: {part2-start}')


main()