from math import sqrt
from pprint import pprint

tiles = {}
edge_to_tile = {}

def left(tile):
    return ''.join([pxl[0] for pxl in tile])

def right(tile):
    return ''.join([pxl[-1] for pxl in tile])

def bottom(tile):
    return tile[-1]

def top(tile):
    return tile[0]

def rotate_tile(tile):
    xs = []
    for i in range(len(tile)):
        s = ''.join(x[i] for x in tile)
        xs.append(s)
    return vert_flip(xs)

def vert_flip(tile):
    return list(reversed(tile))

def horiz_flip(tile):
    return [''.join(list(reversed(row))) for row in tile]

def generate_edges():
    for tile_id, tile in tiles.items():
        l = left(tile)
        r = right(tile)
        l_rev = l[::-1]
        r_rev = r[::-1]
        t = top(tile)
        b = bottom(tile)
        t_rev = t[::-1]
        b_rev = b[::-1]
        edge_to_tile[l] = edge_to_tile.get(l, []) + [tile_id]
        edge_to_tile[r] = edge_to_tile.get(r, []) + [tile_id]
        edge_to_tile[l_rev] = edge_to_tile.get(l_rev, []) + [tile_id]
        edge_to_tile[r_rev] = edge_to_tile.get(r_rev, []) + [tile_id]
        edge_to_tile[t] = edge_to_tile.get(t, []) + [tile_id]
        edge_to_tile[b] = edge_to_tile.get(b, []) + [tile_id]
        edge_to_tile[t_rev] = edge_to_tile.get(t_rev, []) + [tile_id]
        edge_to_tile[b_rev] = edge_to_tile.get(b_rev, []) + [tile_id]
        
def find_corners():
    possible_edges = {}
    for edge in edge_to_tile:
        if len(edge_to_tile[edge]) < 2:
            possible_edges[edge_to_tile[edge][0]] = possible_edges.get(edge_to_tile[edge][0], []) + [edge]
    corners = []
    for tile_id, edge in possible_edges.items():
        if len(edge) == 4:
            corners.append(tile_id)
    return corners
    
def part1(data):
    tile_input = [n for n in data.split('\n\n')]
    for t in tile_input:
        lines = t.splitlines()
        tiles[int(lines[0][5:9])] = lines[1:]
    generate_edges()
    result = 1
    corners = find_corners()
    for c in corners:
        result = result * c
    return result

# Rotate/flip tile until tile_edge(tile) matches target_edge
def match_edge(target_edge, tile, tile_edge):
    possible = possible_orientations(tile)
    for p in possible:
        if tile_edge(p) == target_edge:
            return p
    return None
    
# Constructs a row of tiles based on a first tile
def construct_row(row_head, tiles_per_row):
    prev_tile = row_head
    row = [row_head]
    for _ in range(tiles_per_row - 1):
        if edge_to_tile[right(tiles[prev_tile])][0] == prev_tile:
            next_tile = edge_to_tile[right(tiles[prev_tile])][1]
        if edge_to_tile[right(tiles[prev_tile])][1] == prev_tile:
            next_tile = edge_to_tile[right(tiles[prev_tile])][0]
        tiles[next_tile] = match_edge(right(tiles[prev_tile]), tiles[next_tile], left)
        row.append(next_tile)
        prev_tile = next_tile
    return row

# Finds the first tile for the next row (underneath)
def next_row (row_head):
    prev_tile = row_head
    if edge_to_tile[bottom(tiles[prev_tile])][0] == prev_tile:
        next_tile = edge_to_tile[bottom(tiles[prev_tile])][1]
    if edge_to_tile[bottom(tiles[prev_tile])][1] == prev_tile:
        next_tile = edge_to_tile[bottom(tiles[prev_tile])][0]
    tiles[next_tile] = match_edge(bottom(tiles[row_head]), tiles[next_tile], top)
    return next_tile

# Fully assembles grid into list of strings
def assemble_grid(tile_ids):
    # Strip 4 edges from all tiles
    for row in tile_ids:
        for tile_num in row:
            tile = tiles[tile_num]
            tile = tile[1:-1] # top and bottom
            tile = [pxl[1:-1] for pxl in tile]
            tiles[tile_num] = tile
    # Combine rows
    full_grid = []
    for row in tile_ids:
        for sub_row in range(len(tiles[row[0]])):
            r = ""
            for t in row:
                r += tiles[t][sub_row]
            full_grid.append(r)
    return full_grid
        
def monster_coords():
    monster = [
		'..................#.',
		'#....##....##....###',
		'.#..#..#..#..#..#...'
	]
    coords = set()
    height, width = len(monster), len(monster[0])
    for row in range(height):
        for col in range(width):
            if monster[row][col] == '#':
                coords.add((row, col))
    return coords, width, height
        
def is_monster(slice, monster_coords):
    for x, y in monster_coords:
        if slice[x][y] != '#':
            return False
    return True

def find_monsters(grid):
    coords, width, height = monster_coords()
    num_tags = 0
    num_monsters = 0
    monster_locations = set()
    
    for row in range(len(grid) - height + 1):
        for col in range(len(grid[row]) - width + 1):
            check = [line[col : col + width] for line in grid[row :row + height]]
            if is_monster(check, coords):
                for x_off, y_off in coords:
                    monster_locations.add((row + x_off, col + y_off))
                num_monsters += 1
    if num_monsters == 0:
        return None
    return num_monsters, monster_locations

def possible_orientations(grid):
    possible = []
    g = grid
    for i in range(4):
        g = rotate_tile(g)
        possible.append(g)
        possible.append(vert_flip(g))
        possible.append(horiz_flip(g))
    return possible
        
def print_monsters(grid, monster_locations):
    for row in range(len(grid)):
        r = ""
        for col in range(len(grid[row])):
            if (row, col) in monster_locations:
                r += 'O'
            else:
                r += grid[row][col]
        print(r)
        
def part2(data):
    corners = find_corners()
    c = 0
    top_left = corners[c]
    while len(edge_to_tile[top(tiles[top_left])]) + len(edge_to_tile[left(tiles[top_left])]) > 2:
        top_left = corners[c]
        c += 1
    prev_tile = top_left
    target = top_left
    
    tiles_per_row = int(sqrt(len(tiles))) # assumes square grid
    tile_id_grid = []
    for r in range(tiles_per_row):
        row = construct_row(target, tiles_per_row)
        tile_id_grid.append(row)
        if r < tiles_per_row - 1: # ignore next row if its the last
            target = next_row(target)
    full_grid = assemble_grid(tile_id_grid)
    
    # Find the orientation with monsters
    possible = possible_orientations(full_grid)
    num_monsters = 0
    for p in possible:
        monsters_found = find_monsters(p)
        if monsters_found:
            num_monsters, monster_locations = monsters_found
            print_monsters(full_grid, monster_locations)
            break
        
    total_waters = 0
    for row in full_grid:
        total_waters += row.count('#')
    return total_waters - num_monsters * len(monster_coords()[0])
    