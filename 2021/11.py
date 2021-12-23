import itertools


def run_step(grid):
    # first increase energy levels of all
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            grid[i][j] += 1
    
    # recursively execute flashes        
    flashed_coords = set()
    execute_flashes(grid, flashed_coords)
    
    # set flashed coords to 0
    for x, y in flashed_coords:
        grid[x][y] = 0
        
    # return number of flashes from this step
    return len(flashed_coords)
        
    
def execute_flashes(grid, flashed_coords):
    flashed = False
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (i,j) not in flashed_coords and grid[i][j] > 9:
                flashed_coords.add((i,j))
                flashed = True
                for dx, dy in list(itertools.product(range(-1,2), repeat=2)):
                    if dx == dy == 0: continue
                    if 0 <= j + dx < len(grid[0]) and 0 <= i + dy < len(grid):
                        grid[i+dy][j+dx] += 1
    if flashed:
        execute_flashes(grid, flashed_coords)
    
    
def part1(data):
    grid = [list(map(int, line)) for line in data.splitlines()]
    flash_count = 0
    for _ in range(100):
        flash_count += run_step(grid)
    return flash_count


def part2(data):
    grid = [list(map(int, line)) for line in data.splitlines()]
    grid_size = len(grid) * len(grid[0])
    step = 1
    while run_step(grid) < grid_size:
        step += 1
    return step
