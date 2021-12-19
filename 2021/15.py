import heapq


def parse_input(data):
    grid = [list(map(int, list(line))) for line in data.splitlines()]
    return grid
    
    
def part1(data):
    grid = parse_input(data)
    dp = [[float('inf') for _ in range(len(grid[0]))] for _ in range(len(grid))]
    dp[0][0] = 0
    for r in range(1, len(grid)):
        dp[r][0] = dp[r-1][0] + grid[r][0]
    for c in range(1, len(grid[0])):
        dp[0][c] = dp[0][c-1] + grid[0][c]
    for r in range(1, len(grid)):
        for c in range(1, len(grid[0])):
            dp[r][c] = min(dp[r - 1][c], dp[r][c-1]) + grid[r][c]
    return dp[-1][-1]


def get_cost(x, y, grid):
    dx = x // len(grid[0])
    dy = y // len(grid)
    offset = dx + dy
    new_cost = grid[y % len(grid)][x % len(grid[0])] + offset
    return new_cost % 10 + new_cost // 10


def find_lowest_cost(grid, reps=1):
    pq = [(0,0,0)]
    dists = {}
    while pq:
        cost, x, y = heapq.heappop(pq)
        if (x,y) in dists:
            continue
        dists[(x,y)] = min(dists.get((x,y), float('inf')), cost)
        for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            udx = x + dx
            udy = y + dy
            if 0 <= udx < len(grid[0] * reps) and 0 <= udy < (len(grid) * reps) and (udx, udy) not in dists:
                heapq.heappush(pq, (cost + get_cost(udx, udy, grid), udx, udy))
    return dists[(len(grid[0]) * reps - 1, len(grid) * reps - 1)]


def part2(data):
    grid = parse_input(data)
    return find_lowest_cost(grid, 5)
