def track_vents(vents, with_diag):
    grid = [[0 for _ in range(1000)] for _ in range(1000)]
    for vent in vents:
        start, end = vent.split(' -> ')
        add_vent(grid, start, end, with_diag)
    return total_points(grid)

            
def total_points(grid):
    num_safe_points = 0
    for y in range(len(grid)):
        for x in range(len(grid)):
            if grid[y][x] >= 2:
                num_safe_points += 1
    return num_safe_points

            
def add_vent(grid, start, end, with_diag):
    start_x, start_y = list(map(int, start.split(',')))
    end_x, end_y = list(map(int, end.split(',')))

    if start_y == end_y:
        for x in range(min(start_x, end_x), max(start_x, end_x) + 1):
            grid[start_y][x] += 1
    elif start_x == end_x:
        for y in range(min(start_y, end_y), max(start_y, end_y) + 1):
            grid[y][start_x] += 1
    elif with_diag: # TODO: cleanup
        if end_x > start_x:
            for x in range(start_x, end_x + 1):
                dx = x - start_x
                if end_y > start_y:
                    grid[start_y + dx][x] += 1
                else:
                    grid[start_y - dx][x] += 1
        else:
            for x in range(start_x, end_x - 1, -1):
                dx = abs(x - start_x)
                if end_y > start_y:
                    grid[start_y + dx][x] += 1
                else:
                    grid[start_y - dx][x] += 1    
                    
        
def part1(data):
    vents = data.splitlines()
    return track_vents(vents, False)


def part2(data):
    vents = data.splitlines()
    return track_vents(vents, True)
