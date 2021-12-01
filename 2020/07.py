parent_graph = {}  # part 1
child_graph = {}  # part 2


def parse_rule_p1(rule):
    rule = rule.replace('bags', 'bag').replace('.', '')
    parent, children = rule.split(' contain ')
    children = [c.split(' ', 1)[1] for c in children.split(', ')]
    for c in children:
        if c not in parent_graph:
            parent_graph[c] = set()
        parent_graph[c].add(parent)


def find_parents(bag, parent_set):
    if bag not in parent_graph:
        return
    for parent in parent_graph[bag]:
        parent_set.add(parent)
        find_parents(parent, parent_set)


def part1(data):
    rules = [n for n in data.splitlines()]
    for r in rules:
        parse_rule_p1(r)
    found_parents = set()
    find_parents('shiny gold bag', found_parents)
    return len(found_parents)


def parse_rule_p2(rule):
    rule = rule.replace('bags', 'bag').replace('.', '')
    parent, children = rule.split(' contain ')
    children = children.split(', ')

    if parent not in child_graph:
        child_graph[parent] = set()
    for c in children:
        count, bag_name = c.split(' ', 1)
        if 'no other bag' in c:
            count = "0"
        child_graph[parent].add((bag_name, int(count)))


def count_children(bag):
    if bag not in child_graph:
        return 0
    total = 0
    for child in child_graph[bag]:
        name, count = child
        total += count * (count_children(name) + 1)
    return total


def part2(data):
    rules = [n for n in data.splitlines()]
    for r in rules:
        parse_rule_p2(r)
    return (count_children('shiny gold bag'))
