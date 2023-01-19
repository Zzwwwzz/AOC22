
from collections import deque

def readFile():
    with open("i/18.txt", "r") as file:
        lines = []
        for line in file.readlines():
            lines.append(tuple(map(int, line.strip().split(","))))
    return lines


def get_neighbours(cube):
    x, y, z = cube
    return [
        (x - 1, y, z),
        (x + 1, y, z),
        (x, y - 1, z),
        (x, y + 1, z),
        (x, y, z - 1),
        (x, y, z + 1),
    ]


def solve1(cubes):
    cubes = frozenset(cubes)
    surface_area = 0
    for cube in cubes:
        neighbours = get_neighbours(cube)
        for n in neighbours:
            if n not in cubes:
                surface_area += 1
    return surface_area


def solve2(cubes):
    cubes = frozenset(cubes)
    min_x, min_y, min_z, max_x, max_y, max_z = 0, 0, 0, 0, 0, 0
    for x, y, z in cubes:
        min_x = min(min_x, x)
        max_x = max(max_x, x)
        min_y = min(min_y, y)
        max_y = max(max_y, y)
        min_z = min(min_z, z)
        max_z = max(max_z, z)
    min_x -= 1
    min_y -= 1
    min_z -= 1
    max_x += 1
    max_y += 1
    max_z += 1

    water_points = set()
    q = deque()
    q.append((min_x, min_y, min_z))
    while q:
        x, y, z = q.popleft()
        if (x, y, z) in water_points:
            continue
        water_points.add((x, y, z))
        neighbours = get_neighbours((x, y, z))
        for nx, ny, nz in neighbours:
            if min_x <= nx <= max_x and min_y <= ny <= max_y and min_z <= z <= max_z:
                if (nx, ny, nz) not in cubes:
                    q.append((nx, ny, nz))

    lava_points = set()
    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            for z in range(min_z, max_z + 1):
                if (x, y, z) not in water_points:
                    lava_points.add((x, y, z))
    return solve1(lava_points)

def main():
    data = readFile()
    print(solve1(data))
    print(solve2(data))

main()