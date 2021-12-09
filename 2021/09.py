import math


def is_low_point(x, y, grid):
    center = grid[y][x] 
    if y + 1 < len(grid) and grid[y+1][x] <= center:
        return False
    if y - 1 >= 0 and grid[y-1][x] <= center:
        return False
    if x + 1 < len(grid[0]) and grid[y][x+1] <= center:
        return False
    if x - 1 < len(grid[0]) and grid[y][x-1] <= center:
        return False
    return True


def find_low_points(grid):
    low_points = []
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if is_low_point(x, y, grid):
                low_points.append((x,y))
    return low_points


def part1(data):
    grid = [[int(n) for n in row] for row in data.splitlines()]
    return sum([(grid[y][x] + 1) for x, y in find_low_points(grid)])
    
    
def make_basin(x, y, grid, basin):
    if x < 0 or y < 0 or x >= len(grid[0]) or y >= len(grid):
        return
    if grid[y][x] == 9 or (x,y) in basin:
        return
    else:
        basin.add((x,y))
        make_basin(x + 1, y, grid, basin)
        make_basin(x - 1, y, grid, basin)
        make_basin(x, y + 1, grid, basin)
        make_basin(x, y - 1, grid, basin)
        
    
def find_basin_sizes(grid):
    low_points = find_low_points(grid)
    basins = []
    for x, y in low_points:
        basin = set()
        make_basin(x, y, grid, basin)
        basins.append(len(basin))
    return basins
        

def part2(data):
    grid = [[int(n) for n in row] for row in data.splitlines()]
    return math.prod(sorted(find_basin_sizes(grid), reverse=True)[:3])
    