file = open("input.txt", "r")
expenses = list();

for line in file:
    expenses.append(int(line))

# 952 * 820 * 248 = 193598720
for number in expenses:
    for otherNumber in expenses:
        for anotherNumber in expenses:
            if number + otherNumber + anotherNumber == 2020:
                print(number * otherNumber * anotherNumber)
