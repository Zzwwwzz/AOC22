ROW = 2000000
MAXROW = 4000000

def read_file():
    #data = [[sensors][beacons][distances]]
    data = []
    sensors = []
    beacons = []
    distances = []

    with open('i/15.txt', 'r', encoding="utf-8") as f:
        for line in f:
            line = line.strip().split(":")
            sx = int(line[0].split(",")[0].split("=")[-1])
            sy = int(line[0].split(",")[1].split("=")[-1])
            bx = int(line[1].split(",")[0].split("=")[-1])
            by = int(line[1].split(",")[1].split("=")[-1])
            distance  = abs(sx-bx) + abs(sy-by)

            sensors.append((sx,sy))
            beacons.append((bx,by))
            distances.append((distance))

        data.append(sensors)
        data.append(beacons)
        data.append(distances)
    return data


def valid(x,y,data):
    for i in range(len(data[0])):
        dxy = abs(x-data[0][i][0])+abs(y-data[0][i][1])
        if dxy<=data[2][i]:
            return False
    return True



def p1(data):
    maxl = []
    minl = []
    for i in range(len(data[0])):
        maxl.append(data[0][i][0] - abs(ROW-data[0][i][1]) + data[2][i])
        minl.append(data[0][i][0] + abs(ROW-data[0][i][1]) - data[2][i])

    print(max(maxl)-min(minl))


def p2(data):
    for i in range(len(data[0])):
        for dx in range(data[2][i]+2):
            dy = (data[2][i]+1)-dx
            for signx, signy in [(-1,-1),(-1,1),(1,-1),(1,1)]:
                x = data[0][i][0]+(dx*signx)
                y = data[0][i][1]+(dy*signy)                
                if not(0<=x<=MAXROW and 0<=y<=MAXROW):
                    continue
                assert abs(x-data[0][i][0])+abs(y-data[0][i][1])==data[2][i]+1
                if valid(x,y,data):
                    print(x*MAXROW + y)
                    break
            else: continue
            break
        else: continue
        break


def main():
    data = read_file()
    #print(data)
    p1(data)
    p2(data)

main()