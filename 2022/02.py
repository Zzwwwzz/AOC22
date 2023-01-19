with open("i/2.txt") as file:
    data = file.read().replace(' ','').splitlines()

part1 = ['0','BX','CY','AZ','AX','BY','CZ','CX','AY','BZ']
part2 = ['0','BX','CX','AX','AY','BY','CY','CZ','AZ','BZ']

print(f'part1: {sum(map(part1.index, data))}')
print(f'part2: {sum(map(part2.index, data))}')