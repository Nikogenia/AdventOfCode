with open("calibration.txt", "r") as file:
    lines = file.readlines()

result = 0

for line in lines:
    first = ""
    last = ""
    for char in line:
        if char in "0123456789":
            if first == "":
                first = char
                last = char
            else:
                last = char
    number = int(first + last)
    print(line, first, last, number)
    result += number

print(result)

