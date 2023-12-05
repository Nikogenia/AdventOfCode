with open("games.txt", "r") as file:
    lines = file.readlines()

result = 0

for line in lines:

    red = 0
    green = 0
    blue = 0
    title, sets = line.split(":")
    game = int(title.split(" ")[1])

    for cubes in sets.split(";"):
        for colors in cubes.split(","):

            count, color = colors.strip().split(" ")
            
            if color == "red" and int(count) > red:
                red = int(count)
            if color == "green" and int(count) > green:
                green = int(count)
            if color == "blue" and int(count) > blue:
                blue = int(count)

    power = red * green * blue
    result += power

print(result)

