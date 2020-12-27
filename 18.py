add = lambda x, y: x + y
mult = lambda x, y: x * y

def compute_part_1(line):
    total = 0
    line = list(line.replace(' ', ''))[::-1]
    op = add
    open_paren = 0
    paren_str = ""
    while line:
        curr = line.pop()
        if curr == '(':
            open_paren += 1
        if curr == ')':
            open_paren -= 1
            if open_paren == 0:
                curr = compute_part_1(paren_str[1:])
                paren_str = ''
        if open_paren > 0:
            paren_str += curr
        elif curr == '+':
            op = add
        elif curr == '*':
            op = mult
        elif str(curr).isdigit():
            total = op(total, int(curr))
    return total

def compute_part_2(line):
    stack = []
    line = list(line.replace(' ', ''))[::-1]
    op = add
    open_paren = 0
    paren_str = ""
    while line:
        curr = line.pop()
        if curr == '(':
            open_paren += 1
        if curr == ')':
            open_paren -= 1
            if open_paren == 0:
                curr = str(compute_part_2(paren_str[1:]))
                paren_str = ''
        if open_paren > 0:
            paren_str += curr
        elif curr == '+':
            op = add
            continue
        elif curr == '*':
            op = mult
            continue
        elif op == add and str(curr).isdigit():
            if stack:
                stack.append(str(stack.pop()) + '+' + str(curr))
            else:
                stack.append('0' + '+' + str(curr))
        elif curr != '(' and curr!= ')':
            stack.append(curr)
    for i in range(len(stack)):
        stack[i] = str(eval(stack[i]))
    return eval('*'.join(stack))

def part1(data):
    lines = [n for n in data.splitlines()]
    total = 0
    for line in lines:
        total += compute_part_1(line)
    return total
    
def part2(data):
    lines = [n for n in data.splitlines()]
    total = 0
    for line in lines:
        total += compute_part_2(line)
    return total
