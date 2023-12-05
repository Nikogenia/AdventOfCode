with open("calibration.txt", "r") as file:
    lines = file.readlines()

DIGITS = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

result = 0

for line in lines:
    first = ""
    last = ""
    word = ""
    for char in line:
        if char in "0123456789":
            if first == "":
                first = char
                last = char
            else:
                last = char
            word = ""
            continue
        word += char
        for name, value in DIGITS.items():
            if name in word:
                if first == "":
                    first = value
                    last = value
                else:
                    last = value
                word = word[-len(name):]
                break
    number = int(first + last)
    print(line, first, last, number, word)
    result += number

print(result)

