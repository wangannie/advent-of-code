def execute(instr, line_index, flip_index, acc, seen):
    if line_index >= len(instr): # reached the end
        return (acc, True)
    op, arg = instr[line_index]
    if line_index in seen: # loop found
        return (acc, False)
    seen.add(line_index)
    if (line_index == flip_index and op == 'jmp') or op == 'nop':
        return execute(instr, line_index + 1, flip_index, acc, seen)
    elif (line_index == flip_index and op == 'nop') or op == 'jmp':
        return execute(instr, line_index + arg, flip_index, acc, seen)
    elif op == 'acc':
        return execute(instr, line_index + 1, flip_index, acc + arg, seen)


def parse_instr(data):
    rules = [n for n in data.splitlines()]
    instr = {}
    for i in range(len(rules)):
        op, arg = rules[i].split(' ')
        arg = int(arg.replace('+', ''))
        instr[i] = (op, arg)
    return instr


def part1(data):
    instr = parse_instr(data)
    accumulator, _ = execute(instr, 0, -1, 0, set())
    return accumulator


def part2(data):
    instr = parse_instr(data)
    for i in range(len(instr)):
        if instr[i][0] == 'nop' or instr[i][0] == 'jmp':
            accumulator, reached_end = execute(instr, 0, i, 0, set())
            if reached_end:
                return accumulator