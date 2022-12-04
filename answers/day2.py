import string

with open('../inputs/day2.txt') as f:
    data = f.readlines()

# Removes the newline character from the end of each line
lines = [i.replace('\n', '') for i in data]
score = 0
for line in lines:
    opp = string.ascii_uppercase.index(line.split(' ')[0]) + 1
    you = string.ascii_uppercase.index(line.split(' ')[1]) - 22
    print(opp, you)
