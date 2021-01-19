from collections import OrderedDict


def check_tickets(tickets, rules):
    invalid = 0
    for t in tickets:
        found = False
        for r in rules:
            if t in r:
                found = True
                break
        if not found:
            invalid += t
    return invalid


def decode_ticket(tickets, named_rules, possible, impossible):
    invalid = 0
    for i in range(len(tickets)):
        for rule in named_rules:
            found = False
            for sub_rng in named_rules[rule]:
                if tickets[i] in sub_rng:
                    found = True
                    break
            poss = possible.get(i, set())
            imposs = impossible.get(i, set())
            if found:
                if rule not in imposs:
                    poss.add(rule)
            else:
                if rule in poss:
                    poss.remove(rule)
                imposs.add(rule)
            possible[i] = poss
            impossible[i] = imposs
        if not found:
            invalid += tickets[i]
    return invalid


def parse_range(rng):
    splt = rng.split(' or ')
    ranges = []
    for r in splt:
        start, end = map(int, r.split('-'))
        ranges.append(range(start, end + 1))
    return ranges


def parse_rules(rules):
    rules = rules.splitlines()
    ranges = [r.split(': ')[1] for r in rules]
    rules = []
    for r in ranges:
        rules.extend(parse_range(r))
    return rules


def parse_rules_names(rules):
    rules = rules.splitlines()
    named_rules = OrderedDict()
    for r in rules:
        name, ranges = r.split(': ')
        named_rules[name] = parse_range(ranges)
    return named_rules


def part1(data):
    sections = [n for n in data.split('\n\n')]
    rules, your, nearby = sections

    nearby = nearby.split('\n')[1:]
    nearby = [[int(num) for num in n.split(',')] for n in nearby]
    rules = parse_rules(rules)
    failed = 0
    for n in nearby:
        failed += check_tickets(n, rules)
    return failed


def decode_rules(possible, my_ticket):
    s = sorted(possible, key=possible.get)
    matches = {}
    for index in s:
        if len(possible[index]) > 0:
            matches[index] = sorted(list(possible[index]))[0]
            for i in range(len(possible)):
                if matches[index] in possible[i]:
                    possible[i].remove(matches[index])
    product = 1
    for m in matches:
        if 'departure' in matches[m]:
            print(m, matches[m])
            product *= my_ticket[m]
    return product


def part2(data):
    sections = [n for n in data.split('\n\n')]
    rules, my_ticket, nearby = sections
    my_ticket = [int(n) for n in my_ticket.split('\n')[1].split(',')]
    nearby = nearby.split('\n')[1:]
    nearby = [[int(num) for num in n.split(',')] for n in nearby]
    named_rules = parse_rules_names(rules)
    rules = parse_rules(rules)
    
    nearby = list(filter(lambda n: check_tickets(n, rules) == 0, nearby))
    possible = OrderedDict()
    impossible = {}
    for ticket in nearby:
        decode_ticket(ticket, named_rules, possible, impossible)
    return decode_rules(possible, my_ticket)


# CORRECT DECODING FOR PART 2
# 11 departure location
# 7 departure date
# 16 departure time
# 4 departure track
# 14 departure station
# 2 departure platform
# ANSWER: 239727793813
