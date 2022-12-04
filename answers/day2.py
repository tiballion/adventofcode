import string

with open('../inputs/day2.txt') as f:
    data = f.readlines()


def get_score(line):
    opp = string.ascii_uppercase.index(line.split(' ')[0]) + 1
    you = string.ascii_uppercase.index(line.split(' ')[1]) - 22
    # Rock = 1
    # Paper = 2
    # Scissors = 3
    if opp == you:
        return you + 3
    elif (opp == 1 and you == 3) or (opp == 2 and you == 1) or (opp == 3 and you == 2):
        return you
    else:
        return you + 6


# Removes the newline character from the end of each line
lines = [i.replace('\n', '') for i in data]
score = sum([get_score(i) for i in lines])
print(score)
