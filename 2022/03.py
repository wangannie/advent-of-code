def get_priority(c):
    ord_c = ord(c)
    if ord_c >= ord("a"):
        return ord_c - 96
    return ord_c - 38

def sack_priority(sack):
    midpt = len(sack) // 2
    first = set(sack[:midpt])
    sec = set(sack[midpt:])
    common = list(first.intersection(sec))
    return get_priority(common[0])
    
def part1(data):
    rounds = data.splitlines()
    total_priority = 0
    for r in rounds:
        total_priority += sack_priority(r)
    return total_priority

def part2(data):
    rounds = data.splitlines()
    total_score = 0
    i = 0
    round = set()
    while i < len(rounds):
        if i % 3 == 0:
            round = set(rounds[i])
        else:
            round = round.intersection(set(rounds[i]))
        if i % 3 == 2:
            total_score += get_priority(list(round)[0])
            round = set()
        i += 1
    return total_score
    

