def read_file():
    return [m.split() for m in open('i/10.txt').readlines()]


def first(data):
    signals = [20,60,100,140,180,220]
    xvalues = []
    x=1
    cycle=0

    for ins in data:
        if len(ins) == 1:
            cycle+=1
            if cycle in signals:
                xvalues.append(x)
        else:
            for _ in range(2):
                cycle+=1
                if cycle in signals:
                    xvalues.append(x)   
            x+=int(ins[1])
   
    print(sum([a*b for a,b in zip(signals,xvalues)]))


def second(data):
    ans=""
    x=1
    cycle=0

    for ins  in data:
        if len(ins) == 1:
            cycle+=1
            ans+=check_char(x,cycle)
        else:
            for _ in range(2):
                cycle+=1
                ans+=check_char(x,cycle) 
            x+=int(ins[1])
    print(*[ans[i:i+40] for i in range(0, len(ans), 40)],sep="\n")


def check_char(x,cycle):
    sprite = [x-1,x,x+1]
    if (cycle%40)-1 in sprite and (cycle%40)-1>=0:
        return "⬜"
    return "⬛"


def main():
    data = read_file()
    first(data)
    second(data)


main()