empty = ('L', 'O')
# O means used to be empty, becoming occupied at end of state update

occupied = ('#', 'E')
# E means used to be occupied, becoming empty at end of state update

floor = '.'


# For part 1
def adjacent_sides(seats, x, y, r_off, c_off):
    if c_off + y >= 0 and c_off + y < len(seats[0]) and r_off + x >= 0 and r_off + x < len(seats):
        return seats[r_off + x][c_off + y] in occupied
    return 0


# For part 2
def visible_sides(seats, x, y, row_inc, col_inc):
    max_x, max_y = len(seats), len(seats[0])
    r_off = row_inc
    c_off = col_inc
    while c_off + y >= 0 and c_off + y < max_y and r_off + x >= 0 and r_off + x < max_x:
        if seats[r_off + x][c_off + y] in occupied:
            return 1
        if seats[r_off + x][c_off + y] in empty:
            break
        c_off += col_inc
        r_off += row_inc
    return 0


def count_occupied(seats, x, y, check_sides):
    dimensions = [-1, 0, 1]
    count = 0
    for r in dimensions:
        for c in dimensions:
            if not (c == 0 and r == 0):
                count += check_sides(seats, x, y, r, c)
    return count


def update_state(seats, sides_func, max_occ):
    state_changed = False
    for row in range(len(seats)):
        for col in range(len(seats[row])):
            if seats[row][col] is not floor:
                num_occupied = count_occupied(seats, row, col, sides_func)
                if seats[row][col] in empty and num_occupied == 0:
                    seats[row][col] = empty[1]  # flagged to become occupied
                    state_changed = True
                elif seats[row][col] in occupied and num_occupied >= max_occ:
                    seats[row][col] = occupied[1]  # flagged to become empty
                    state_changed = True
    if state_changed:  # Finally, update temporary 'O' and 'E' indicators
        for row in range(len(seats)):
            for col in range(len(seats[row])):
                if seats[row][col] is occupied[1]:
                    seats[row][col] = empty[0]
                elif seats[row][col] is empty[1]:
                    seats[row][col] = occupied[0]
        update_state(seats, sides_func, max_occ)


def part1(data):
    rows = [n for n in data.splitlines()]
    seats = [list(row) for row in rows]
    update_state(seats, adjacent_sides, 4)
    return sum(row.count(occupied[0]) for row in seats)


def part2(data):
    rows = [n for n in data.splitlines()]
    seats = [list(row) for row in rows]
    update_state(seats, visible_sides, 5)
    return sum(row.count(occupied[0]) for row in seats)
