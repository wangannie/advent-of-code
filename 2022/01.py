import heapq


def count_calories(data):
    elves_calories = data.split('\n\n')
    max_calories = float('-inf')
    for elf_calories in elves_calories:
        calories = elf_calories.splitlines()
        total_calories = sum(map(int, calories))
        max_calories = max(max_calories, total_calories)
    return max_calories

def top_three_calories(data):
    elves_calories = data.split('\n\n')
    heap = []
    for elf_calories in elves_calories:
        calories = elf_calories.splitlines()
        total_calories = sum(map(int, calories))
        if len(heap) < 3:
            heapq.heappush(heap, total_calories)
        else:
            heapq.heappushpop(heap, total_calories)
    return sum(heap)
    
def part1(data):
    return count_calories(data)


def part2(data):
    return top_three_calories(data)
