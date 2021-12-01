def initialize(data, dim):
    active = set()
    for i, row in enumerate(data):
        for j, val in enumerate(row):
            if val == '#':
                active.add(tuple([i, j] + [0] * (dim - 2)))
    return active


def count_neighbors_3d(active, curr, nbrs):
    x, y, z = curr
    count = 0
    offsets = [-1, 0, 1]
    for x_off in offsets:
        for y_off in offsets:
            for z_off in offsets:
                checking = tuple([x_off + x, y_off + y, z_off + z])
                if checking in active:
                    if checking != curr:
                        count += 1
                else:
                    nbrs[checking] = nbrs.get(checking, 0) + 1
    return count


def count_neighbors_4d(active, curr, nbrs):
    x, y, z, w = curr
    count = 0
    offsets = [-1, 0, 1]
    for x_off in offsets:
        for y_off in offsets:
            for z_off in offsets:
                for w_off in offsets:
                    checking = tuple(
                        [x_off + x, y_off + y, z_off + z, w_off + w])
                    if checking in active:
                        if checking != curr:
                            count += 1
                    else:
                        nbrs[checking] = nbrs.get(checking, 0) + 1
    return count


def cycle(active, dimension, cycles):
    for _ in range(cycles):
        nbrs = {}
        keep_active = set()
        for a in active:
            active_nbrs = 0
            if dimension == 3:
                active_nbrs = count_neighbors_3d(active, a, nbrs)
            if dimension == 4:
                active_nbrs = count_neighbors_4d(active, a, nbrs)
            if active_nbrs in range(2, 4):
                keep_active.add(a)
        turn_active = set([
            coord for coord, act_nbrs in nbrs.items()
            if coord not in active and act_nbrs == 3
        ])
        active = turn_active.union(keep_active)
    return len(active)


def part1(data):
    active = initialize(data.splitlines(), 3)
    return cycle(active, 3, 6)


def part2(data):
    active = initialize(data.splitlines(), 4)
    return cycle(active, 4, 6)
