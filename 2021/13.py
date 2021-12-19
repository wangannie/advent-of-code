def construct_grid(dots):
    grid = [['.' for _ in range(1311)] for _ in range(895)]
    for x, y in dots:
        grid[y][x] = '#'
    return grid

    
def fold(instr, grid):
    axis, point = instr.split('=')
    point = int(point)
    if axis == 'y':
        for i in range(point):
            merge_rows(grid[i], grid[point + (point - i)])
        grid = grid[:point]
    else:
        for i in range(point):
            merge_cols(grid, i, point + (point - i))
        for i in range(len(grid)):
            grid[i] = grid[i][:point]
    return grid
    
    
def count_dots(grid):
    dots = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '#':
                dots += 1
    return dots


def merge_cols(grid, dest_idx, src_idx):
    for i in range(len(grid)):
        if grid[i][src_idx] == '#':
            grid[i][dest_idx] = '#'

    
def merge_rows(dest_row, src_row):
    for i in range(len(dest_row)):
        if src_row[i] == '#':
            dest_row[i] = '#'

            
def parse_input(data):
    dots, instr = data.split('\n\n')
    dots = [tuple(map(int, line.split(','))) for line in dots.splitlines()]
    instr = [line.split('fold along ')[1] for line in instr.splitlines()]
    grid = construct_grid(dots)
    return grid, instr
            
            
def part1(data):
    grid, instr = parse_input(data)
    grid = fold(instr[0], grid)
    return count_dots(grid)


def part2(data):
    grid, instr = parse_input(data)
    for i in range(len(instr)):
        grid = fold(instr[i], grid)
    for row in grid:
        print(''.join(row))
