directions = {
    'N': (0, 1),
    'E': (1, 0),
    'S': (0, -1),
    'W': (-1, 0),
}


def manhattan_dist(state):
    x, y, _ = state
    return abs(x) + abs(y)


# Moves ships and waypoints for part 1 and part 2
def move(action, value, start_state):
    start_x, start_y, direction = start_state
    new_x, new_y = start_x, start_y
    if action in directions:
        delta_x, delta_y = directions[action]
    else:
        delta_x, delta_y = directions[direction]
    for _ in range(value):
        new_x += delta_x
        new_y += delta_y
    return (new_x, new_y, direction)


# Updates ship based on part 1 instructions
def update_ship(action, value, start_state):
    start_x, start_y, direction = start_state
    if action == 'R' or action == 'L':
        new_direction = rotate_ship(action, value, direction)
        return (start_x, start_y, new_direction)
    else:
        return move(action, value, start_state)


def rotate_ship(action, value, start_dir):
    clockwise = ['N', 'E', 'S', 'W']
    delta = value // 90
    if action == 'L':
        delta *= -1
    index = clockwise.index(start_dir)
    index += delta
    return clockwise[index % 4]


# For 'F' action in part 2
def ship_to_waypoint(action, value, ship, waypoint):
    dx, dy, _ = waypoint
    if value * dx >= 0:
        ship = move('E', value * dx, ship)
    else:
        ship = move('W', abs(value * dx), ship)
    if value * dy >= 0:
        ship = move('N', value * dy, ship)
    else:
        ship = move('S', abs(value * dy), ship)
    return ship


def rotate_waypoint(action, value, waypoint):
    x, y, _ = waypoint
    rotations = value // 90
    while rotations > 0:
        if action == 'R':
            temp = x
            x = y
            y = -1 * temp
        else:
            temp = x
            x = -1 * y
            y = temp
        rotations -= 1
    return (x, y, '')


def part1(data):
    rows = [n for n in data.splitlines()]
    ship = (0, 0, 'E')
    for instr in rows:
        action, value = instr[0], int(instr[1:])
        ship = update_ship(action, value, ship)
    return manhattan_dist(ship)


def part2(data):
    rows = [n for n in data.splitlines()]
    ship = (0, 0, 'E')
    waypoint = (10, 1, '')
    for instr in rows:
        action, value = instr[0], int(instr[1:])
        if action == 'R' or action == 'L':
            waypoint = rotate_waypoint(action, value, waypoint)
        elif action in directions:
            waypoint = move(action, value, waypoint)
        else:
            ship = ship_to_waypoint(action, value, ship, waypoint)
    return manhattan_dist(ship)
