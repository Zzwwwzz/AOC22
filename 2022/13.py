from functools import cmp_to_key
from math import prod

def readFile():
    data = [[*map(eval, x.split())] for x in open('i/13.txt').read().split('\n\n')]
    return data

def cmp(l, r):
    match l, r:
        case int(), int():  return (l>r) - (l<r)
        case int(), list(): return cmp([l], r)
        case list(), int(): return cmp(l, [r])
        case list(), list():
            for z in map(cmp, l, r):
                if z: return z
            return cmp(len(l), len(r))

def p1(data):
    return(sum(i for i, p in enumerate(data, 1) if cmp(*p) == -1))

def p2(data):
    packets = sorted(sum(data, [[2], [6]]), key=cmp_to_key(cmp))
    return(prod(i for i, p in enumerate(packets, 1) if p in [[2], [6]]))

def main():
    packets = readFile()
    print(f'Part 1: {p1(packets)}')
    print(f'Part 2: {p2(packets)}')

main()