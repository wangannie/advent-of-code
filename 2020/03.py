def count_trees(rows, right, down):
    width = len(rows[0])
    x, trees = 0, 0
    for i in range(0, len(rows), down):
        if rows[i][x % width] == '#':
            trees += 1
        x += right
    return trees


def part1(data):
    rows = [n for n in data.splitlines()]
    return count_trees(rows, 3, 1)


def part2(data):
    rows = [n for n in data.splitlines()]
    r1 = count_trees(rows, 1, 1)
    r2 = count_trees(rows, 3, 1)
    r3 = count_trees(rows, 5, 1)
    r4 = count_trees(rows, 7, 1)
    r5 = count_trees(rows, 1, 2)
    return r1 * r2 * r3 * r4 * r5
