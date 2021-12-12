ref = {
    '}': '{',
    ')': '(',
    ']': '[',
    '>': '<',
}

syntax_points = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}

autocomplete_points = {
    '(': 1,
    '[': 2,
    '{': 3,
    '<': 4,
}

def get_corruption_score(line):
    stack = []
    for c in line:
        if c in ref:
            if len(stack) > 0 and stack[-1] == ref[c]:
                stack.pop()
            else:
                return syntax_points[c]
        else:
            stack.append(c)
    return 0


def get_autocomplete_score(line):
    stack = []
    for c in line:
        if c in ref:
            if len(stack) > 0 and stack[-1] == ref[c]:
                stack.pop()
            else:
                return 0
        else:
            stack.append(c)
    return completion_str_score(stack)

    
def completion_str_score(stack):
    total = 0
    while stack:
        total *= 5
        total += autocomplete_points[stack.pop()]
    return total
    
    
def part1(data):
    lines = data.splitlines()
    total_score = 0
    for line in lines:
        total_score += get_corruption_score(line)
    return total_score


def part2(data):
    lines = data.splitlines()
    autocomplete_scores = []
    for line in lines:
        score = get_autocomplete_score(line)
        if score > 0:
            autocomplete_scores.append(score)
    return sorted(autocomplete_scores)[len(autocomplete_scores) // 2]
    