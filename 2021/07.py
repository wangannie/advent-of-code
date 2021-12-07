import math


def find_best_alignment_cost(positions, cost_fn):
    min_cost = float('inf')
    for alignment_point in range(min(positions), max(positions) + 1):
        cost = 0
        for p in positions:
            cost += cost_fn(p - alignment_point)
        min_cost = min(min_cost, cost)
    return min_cost


def part1(data):
    positions = list(map(int, data.split(',')))
    return find_best_alignment_cost(positions, abs)
    

def part2(data):
    positions = list(map(int, data.split(',')))
    return find_best_alignment_cost(positions, lambda n: math.comb(abs(n) + 1, 2))
    
