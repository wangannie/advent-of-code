def get_position_part1(commands):
    horiz_pos, depth = 0, 0
    for command in commands:
        dir, dist = command.split()
        dist = int(dist)
        if dir == 'down':
            depth += dist
        elif dir == 'up':
            depth -= dist
        else:
            horiz_pos += dist
    return horiz_pos, depth

def get_position_part2(commands):
    horiz_pos, depth, aim = 0, 0, 0
    for command in commands:
        dir, x = command.split()
        x = int(x)
        if dir == 'down':
            aim += x
        elif dir == 'up':
            aim -= x
        else:
            horiz_pos += x
            depth += aim * x
    return horiz_pos, depth
                

def part1(data):
    commands = [n for n in data.splitlines()]
    horiz_pos, depth = get_position_part1(commands)
    return horiz_pos * depth


def part2(data):
    commands = [n for n in data.splitlines()]
    horiz_pos, depth = get_position_part2(commands)
    return horiz_pos * depth
    