
rocks = [[(0,0), (1,0), (2,0), (3,0)],        # -
         [(0,1), (1,1), (2,1), (1,0), (1,2)], # +
         [(0,0), (1,0), (2,0), (2,1), (2,2)], # J
         [(0,0), (0,1), (0,2), (0,3)],        # |
         [(0,0), (0,1), (1,0), (1,1)]]        # O

def get_rock_width(rock):
    width = 0
    for coord in rock:
        width = max(width, coord[0]) 
    return width + 1

def check_collision(tower, rock, rockleft, rockbottom, rockwidth):
    if rockbottom < 0:
        return True
    if rockleft < 0 or rockleft + rockwidth > 7:
        return True
    for coord in rock:
        if (coord[0] + rockleft, coord[1] + rockbottom) in tower:
            return True
    return False

def get_surface_map(tower, towerheight):
    surface = []
    for x in range(0, 7):
        y = towerheight
        while (x, y) not in tower and y > 0:
            y -= 1
        surface.append(towerheight - y)
    return tuple(surface)

def play_rocktris(wind, max_rocks):
    tower = set()
    rockcount = 0
    towerheight = 0
    windpos = 0
    newrock = 0
    height_adjust = 0
    savedstates = {}
    while rockcount < max_rocks:
        rock = rocks[newrock]
        w = get_rock_width(rock)
        rockbottom = towerheight + 3 
        rockleft = 2
        moving = True
        while moving:
            oldrockleft = rockleft
            if wind[windpos] == ">":
                rockleft += 1
            elif rockleft > 0:
                rockleft -= 1
            if check_collision(tower, rock, rockleft, rockbottom, w):
                rockleft = oldrockleft
            windpos = (windpos + 1) % len(wind)

            rockbottom -= 1
            if check_collision(tower, rock, rockleft, rockbottom, w):
                rockbottom += 1
                moving = False
                for coord in rock:
                    tower.add((coord[0] + rockleft, coord[1] + rockbottom))
                    towerheight = max(towerheight, coord[1] + rockbottom + 1)

        currstate = (get_surface_map(tower, towerheight), windpos, newrock)
        if currstate in savedstates: 
            last_rockcount, last_height = savedstates[currstate]
            height_diff = towerheight - last_height
            count_diff = rockcount - last_rockcount
            repeats = (max_rocks - rockcount) // count_diff
            height_adjust += height_diff * repeats
            rockcount += count_diff * repeats 
        savedstates[currstate] = (rockcount, towerheight)

        newrock = (newrock + 1) % 5
        rockcount += 1
    return towerheight + height_adjust

def main():
    data = open('i/17.txt', 'r').read().rstrip()

    print(f"pt 1: {play_rocktris(data, 2022)}")
    print(f"fpt 2: {play_rocktris(data, 1000000000000)}")

main()