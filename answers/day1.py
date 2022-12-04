def get_data():
    """Reads the input file and returns a list of lines"""
    with open('../inputs/day1.txt') as f:
        data = f.readlines()
    return data


def get_calories(data):
    """Returns a list of lists of the calories of each elf"""
    res = []
    calories = []
    for line in data:
        if line == '\n':
            res.append(calories)
            calories = []
        else:
            calories.append(int(line[:-1]))
    return res


def part1(calories):
    maxi = 0
    for i in calories:
        if sum(i) > maxi:
            maxi = sum(i)
    print(maxi)


def part2(calories):
    s = []
    for i in calories:
        t = sum(i)
        s.append(t)
    sort = sorted(s)
    print(sum(sort[-3:]))


def main():
    data = get_data()
    calories = get_calories(data)
    part1(calories)
    part2(calories)


if __name__ == '__main__':
    main()
