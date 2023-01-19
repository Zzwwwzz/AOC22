def readFile():
    return open("i/7.txt").readlines()

def up(stack, sizes):
    sizes.append(stack.pop(-1))
    if stack:
        stack[-1] += sizes[-1]

def main():
    data = readFile()
    stack = []
    sizes = []
    for line in data:
        match line.strip().split():
            case "$", "cd", "..": up(stack, sizes)
            case "$", "cd", _: stack.append(0)
            case "$", _: pass
            case "dir", _: pass
            case size, _: stack[-1] += int(size)

    while stack:
        up(stack, sizes)

    print(sum(s for s in sizes if s <= 100000))
    print(min(s for s in sizes if s >= (max(sizes) - 40000000)))

main()
