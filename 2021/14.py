from collections import Counter


def parse_input(data):
    template, rules = data.split('\n\n')
    rules = {line.split(' -> ')[0] : line.split(' -> ')[1] for line in rules.splitlines()}
    return template, rules


def apply_replacements_naive(template, rules):
    new_str = template[0]
    for end in range(1, len(template)):
        pair = template[end - 1 : end + 1]
        if pair in rules:
            new_str += rules[pair]
        new_str += pair[1]
    return new_str


def apply_replacements_map(pairs, rules):
    for pair, count in pairs.copy().items():
        if pair in rules:
            new_pair_1 = pair[0] + rules[pair]
            new_pair_2 = rules[pair] + pair[1]
            pairs[new_pair_1] = pairs.get(new_pair_1, 0) + count
            pairs[new_pair_2] = pairs.get(new_pair_2, 0) + count
            pairs[pair] -= count
    return pairs


def part1(data):
    template, rules = parse_input(data)
    for _ in range(10):
        template = apply_replacements_naive(template, rules)
    ordered = Counter(template).most_common()
    return ordered[0][1] - ordered[-1][1]


def part2(data):
    template, rules = parse_input(data)
    
    # generate initial pairs from template str
    pairs = {}
    for end in range(1, len(template)):
        pair =  template[end - 1 : end + 1]
        pairs[pair] = pairs.get(pair, 0) + 1
        
    for _ in range(40):
        pairs = apply_replacements_map(pairs, rules)
        
    ltr_counts = {}
    for pair, count in pairs.items():
        if count > 0:
            p1, p2 = pair
            ltr_counts[p1] = ltr_counts.get(p1, 0) + count
            ltr_counts[p2] = ltr_counts.get(p2, 0) + count
            
    sorted_counts = sorted(ltr_counts.items(), key=lambda x: x[1], reverse=True)
    return ((sorted_counts[0][1] + 1) // 2) - ((sorted_counts[-1][1] + 1) // 2)
        
