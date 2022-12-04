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
    """Returns the highest amount of calories"""
    maxi = 0
    for i in calories:
        if sum(i) > maxi:
            maxi = sum(i)
    return maxi


def part2(calories):
    """Returns the sum of the top 3 amount of calories"""
    s = []
    for i in calories:
        t = sum(i)
        s.append(t)
    sort = sorted(s)
    return sum(sort[-3:])


def main():
    data = get_data()
    calories = get_calories(data)
    res1 = part1(calories)
    res2 = part2(calories)
    print(f"Part 1: {res1}")
    print(f"Part 2: {res2}")


if __name__ == '__main__':
    main()
