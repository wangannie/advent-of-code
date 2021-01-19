directions = {
    'e': (1, 0),
    'se': (1, -1),
    'sw': (-1, -1),
    'w': (-1, 0),
    'nw': (-1, 1),
    'ne': (1, 1),
}

def part1(data):
    ids = [n for n in data.splitlines()]
    black_tiles = set()
    for id in ids:
        tile = find_hexagon(parse_line(id), (0,0))
        if tile in black_tiles:
            black_tiles.remove(tile)
        else:
            black_tiles.add(tile)
    return len(black_tiles)

def parse_line(line):
    actions = []
    i = 0
    while i < len(line):
        if line[i] == 'e' or line[i] == 'w':
            actions.append(line[i])
            i += 1
        else:
            actions.append(line[i:i + 2])
            i += 2
    return actions
    
def find_hexagon(actions, start):
    x, y = start
    for a in actions:
        deltaX, deltaY = directions[a]
        if y % 2 == 0 and len(a) > 1 and 'e' in a:
            deltaX = 0
        elif y % 2 == 1 and len(a) > 1 and 'w' in a:
            deltaX = 0
        x += deltaX
        y += deltaY
    return (x, y)

def part2(data):
    ids = [n for n in data.splitlines()]
    # Find initial tile layout
    black_tiles = set()
    for id in ids:
        tile = find_hexagon(parse_line(id), (0,0))
        if tile in black_tiles:
            black_tiles.remove(tile)
        else:
            black_tiles.add(tile)
    # Apply rules for 100 days
    for _ in range(100):
        black_tiles = apply_rules(black_tiles)
    return len(black_tiles)

def neighbors(tile):
    adj = []
    x, y = tile
    for direction, offset in directions.items():
            x_off, y_off = offset
            if y % 2 == 0 and len(direction) > 1 and 'e' in direction:
                x_off = 0
            elif y % 2 == 1 and len(direction) > 1 and 'w' in direction:
                x_off = 0
            adj.append((x + x_off, y + y_off))
    return adj

def apply_rules(black_tiles):
    visited = set()
    fringe = set()
    black_after = black_tiles.copy()
    for tile in black_tiles:
        fringe.add(tile)
        for adj in neighbors(tile):
            fringe.add(adj)
            
    while len(fringe) > 0:
        curr = fringe.pop()
        if curr in visited:
            continue
        black_adj = 0
        for adj in neighbors(curr):
            black_adj += adj in black_tiles
        if curr in black_tiles: # tile is black
            if black_adj == 0 or black_adj > 2:
                black_after.remove(curr)
        elif black_adj == 2: # tile must be white
            black_after.add(curr)
    return black_after
            