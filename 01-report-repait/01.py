file = open("input.txt", "r")
expenses = list();

for line in file:
    expenses.append(int(line))

# 2004 * 16 = 32064
for number in expenses:
    for otherNumber in expenses:
        if number + otherNumber == 2020:
            print(number * otherNumber)
