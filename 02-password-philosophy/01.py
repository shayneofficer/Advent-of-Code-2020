file = open("input.txt", "r")
countOfValidPasswords = 0

for line in file:
    # remove newline
    fixedLine = line.split('\n')[0]

    # split line into rule and password
    (rule, password) = fixedLine.split(": ")

    # split rule into validRange, and character
    (validRange, character) = rule.split(" ")

    # split valid range into min and max
    (minimum, maximum) = validRange.split("-")

    minimum = int(minimum)
    maximum = int(maximum)

    occurences = password.count(character)
    isValid = occurences >= minimum and occurences <= maximum

    if isValid:
        countOfValidPasswords += 1

# 454
print(countOfValidPasswords)
