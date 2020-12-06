from collections import Counter


def count_all_yes(response):
    group_size, response_str = response
    counter = Counter(response_str)
    total = 0
    for count in counter.values():
        if count == group_size:
            total += 1
    return total


def part1(data):
    groups = [n.replace('\n', '') for n in data.split('\n\n')]
    total = 0
    for g in groups:
        total += len(set(g))
    return total


def part2(data):
    groups = [n for n in data.split('\n\n')]
    responses = []
    for g in groups:
        count = len(g.split('\n'))
        combined_str = g.replace('\n', '')
        responses.append((count, combined_str))
    total = 0
    for r in responses:
        total += count_all_yes(r)
    return total
