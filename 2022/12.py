from collections import deque, defaultdict
from timeit import default_timer as timer

def read_file():
    with open("i/12.txt") as f:
        data = f.read().strip().split('\n')
    return data

def solve(data, part):
    h = len(data)
    w = len(data[0])
    for i in range(h):
        for j in range(w):
            if data[i][j] == "S":
                sx, sy = i,j

            elif data[i][j] == "E":
                ex, ey = i,j


    data[sx] = data[sx].replace("S", "a")
    data[ex] = data[ex].replace("E", "z")

    drs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    nummap = [[ord(c)-ord("a") for c in r] for r in data]
    
    dst = defaultdict(lambda : 1000000)
    if part == 1:
        q = deque([(sx,sy)])
    else:
        q = deque([(i,j) for i in range(h) for j in range(w) if nummap[i][j] == 0])

    for x,y in q:
        dst[x,y]=0
    
    ans = 100000
    while len(q)>0:
        cx,cy = q.popleft()
        if (cx,cy) == (ex, ey):
            ans = dst[ex,ey]
            print(ans)
            break
        for dx,dy in drs:
            nx,ny = cx+dx,cy+dy
            if nx in range(h) and ny in range(w):
                if nummap[cx][cy] >= nummap[nx][ny]-1:
                    ndst = dst[cx,cy]+1
                    if ndst < dst[nx,ny]:
                        q.append((nx,ny))
                        dst[nx,ny] = ndst


def main():
    start = timer()
    data = read_file()

    data1 = data.copy()
    data2 = data.copy()

    solve(data1, 1)
    p1 = timer()
    solve(data2, 2)
    p2 = timer()
    print(f'p1: {p1-start}\np2: {p2-p1}\nboth: {p2-start}')

main()