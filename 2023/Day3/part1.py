with open("engine.txt", "r") as file:
    lines = file.readlines()

result = 0

for i, line in enumerate(lines):

    number = ""
    included = False

    for j, char in enumerate(line):

        if char in "0123456789":
            number += char
            if (j > 0 and line[j - 1] not in ".0123456789") or \
                (j < len(line) - 1 and line[j + 1] not in ".0123456789"):
                included = True
            if i > 0:
                if (j > 0 and lines[i - 1][j - 1] not in ".0123456789") or \
                    (lines[i - 1][j] not in ".0123456789") or \
                    (j < len(line) - 1 and lines[i - 1][j + 1] not in ".0123456789"):
                    included = True
            if i < len(lines) - 1:
                if (j > 0 and lines[i + 1][j - 1] not in ".0123456789") or \
                    (lines[i + 1][j] not in ".0123456789") or \
                    (j < len(line) - 1 and lines[i + 1][j + 1] not in ".0123456789"):
                    included = True
            continue

        if number:
            if included:
                result += int(number)
                included = False
            number = ""

print(result)

