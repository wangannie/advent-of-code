from collections import Counter


def simulate_day_brute_force(fish):
    for i in range(len(fish)):
        if fish[i] == 0:
            fish[i] = 6
            fish.append(8)
        else:
            fish[i] -= 1
            
            
def simulate_day(fish):
    new_fish = {}
    for i in range(9):
        if i not in fish:
            continue
        elif i == 0:
            new_fish[6] = fish[i]
            new_fish[8] = fish[i]
        else:
            new_fish[i - 1] = new_fish.get(i-1, 0) + fish[i]
    return new_fish

    
def part1(data):
    fish = list(map(int, data.split(',')))
    for i in range(80):
        simulate_day_brute_force(fish)
    return len(fish)
    

def part2(data):
    fish = Counter(list(map(int, data.split(','))))
    for i in range(256):
        fish = simulate_day(fish)
    return sum(fish.values())
