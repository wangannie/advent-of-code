def search(seat, lo, hi):
    for c in seat:
        if c == 'F' or c == 'L':
            hi = (hi - lo + 1) // 2 + lo - 1
        else:
            lo = hi - (hi - lo + 1) // 2 + 1
    if seat[-1] == 'F' or seat[-1] == 'L':
        return lo
    else:
        return hi


def find_seat_id(seat):
    row = search(seat[:-3], 0, 127)
    col = search(seat[-3:], 0, 7)
    return row * 8 + col


def part1(data):
    rows = [n for n in data.splitlines()]
    max_id = 0
    for r in rows:
        max_id = max(max_id, find_seat_id(r))
    return max_id


def part2(data):
    rows = [n for n in data.splitlines()]
    # seat ids range from 48 to 818
    nums = set([n for n in range(48, 819)])
    for r in rows:
        nums.remove(find_seat_id(r))
    return nums.pop()
