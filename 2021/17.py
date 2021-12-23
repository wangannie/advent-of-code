def launch_probe(x_vel, y_vel, x_range, y_range):
    x_start, x_end = x_range
    y_start, y_end = y_range
    max_height = 0
    x, y = 0, 0
    while x <= x_end and y >= y_start:
        max_height = max(max_height, y)
        if x_start <= x <= x_end and y_start <= y <= y_end:
            return True, max_height
        x += x_vel
        y += y_vel
        if x_vel > 0:
            x_vel -= 1
        elif x_vel < 0:
            x_vel += 1
        y_vel -= 1
    return False, None

    
def parse_input(data):
    ranges = [coord.split('=')[1] for coord in data.split(': ')[1].split(', ')]
    ranges = [list(map(int, r.split('..'))) for r in ranges]
    return (ranges[0][0], ranges[0][1]), (ranges[1][0], ranges[1][1]) # (start_x, end_x), (start_y, end_y)
    
    
def part1(data):
    x_range, y_range = parse_input(data)
    initial_y_vel = y_range[0] * -1 - 1 # initial y vel to reach max height is -1 * (start_y (y_min)) - 1
    for x_vel in range(x_range[1] + 1): # until max x
        reached, max_height = launch_probe(x_vel, initial_y_vel, x_range, y_range)
        if reached:
            return max_height
        

def part2(data):
    x_range, y_range = parse_input(data)
    velocity_count = 0
    for x_vel in range(x_range[1] + 1): # until max x
        for y_vel in range(y_range[0], abs(y_range[0]) + 1):
            if launch_probe(x_vel, y_vel, x_range, y_range)[0]:
                velocity_count += 1

    return velocity_count
