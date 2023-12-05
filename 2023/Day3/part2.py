with open("engine.txt", "r") as file:
    lines = file.readlines()

result = 0

gears = {}

for i, line in enumerate(lines):

    number = ""
    positions = []

    for j, char in enumerate(line):

        if char in "0123456789":
            number += char
            for dx, dy in [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]:
                if 0 <= j + dx < len(line) and 0 <= i + dy < len(lines):
                    if lines[i + dy][j + dx] == "*":
                        if (i + dy, j + dx) not in positions:
                            positions.append((i + dy, j + dx))
            continue

        if number:
            for position in positions:
                if position not in gears:
                    gears[position] = []
                gears[position].append(int(number))
            positions = []
            number = ""

for gear, numbers in gears.items():
    if len(numbers) >= 2:
        ratio = 1
        for number in numbers:
            ratio *= number
        print(gear, numbers, ratio)
        result += ratio
print(result)

