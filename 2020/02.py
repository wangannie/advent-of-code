def parse_rule(rule):
    n1 , rest = rule.split('-')
    n1 = int(n1)
    n2, rest = rest.split(' ', 1)
    n2 = int(n2)
    c, pwd = rest.split(": ")
    return (n1, n2, c, pwd)

def valid_rule_p1(rule):
    n1, n2, c, pwd = rule
    c_count = pwd.count(c)
    if c_count >= n1 and c_count <= n2:
        return True
    return False

def valid_rule_p2(rule):
    n1, n2, c, pwd = rule
    valid = False
    if pwd[n1 - 1] == c:
        valid = not valid
    if pwd[n2 - 1] == c:
        valid = not valid
    return valid

def part1(data):
    rules = [n for n in data.splitlines()]
    valid = 0
    for r in rules:
        if valid_rule_p1(parse_rule(r)):
            valid += 1
    return valid

def part2(data):
    rules = [n for n in data.splitlines()]
    valid = 0
    for r in rules:
        if valid_rule_p2(parse_rule(r)):
            valid += 1
    return valid