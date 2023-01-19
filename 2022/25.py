def readFile():
    with open('i/25.txt', 'r') as file:
        data = file.read()
    return data

def to_decimal(number, decimals, fuels):
    return sum([(5 ** i) * fuels[c] for i, c in enumerate(reversed(number))])

def to_fuel(number, decimals):
    value = []

    while number > 0:
        remainder = number % 5
        if remainder > 2:
            number += remainder
            value.append(decimals[remainder - 5])
        else:
            value.append(str(remainder))

        number //= 5

    return ''.join(reversed(value))

def main():
    data = readFile()
    fuels = { '=': -2, '-': -1, '0': 0, '1': 1, '2': 2 }
    decimals = dict(map(reversed, fuels.items()))

    numbers = []

    for line in data.splitlines():
        numbers.append(to_decimal(line, decimals, fuels))

    print(to_fuel(sum(numbers), decimals))

main()