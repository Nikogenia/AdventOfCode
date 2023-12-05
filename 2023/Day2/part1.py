with open("games.txt", "r") as file:
    lines = file.readlines()

result = 0

for line in lines:

    possible = True
    title, sets = line.split(":")
    game = int(title.split(" ")[1])

    for cubes in sets.split(";"):
        for colors in cubes.split(","):

            count, color = colors.strip().split(" ")
            
            if (color == "red" and int(count) > 12) or \
                (color == "green" and int(count) > 13) or \
                (color == "blue" and int(count) > 14):
                possible = False

    if possible:
        result += game

print(result)

