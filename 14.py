def eval_mask(mask, value, overrides):
    val = list("{0:b}".format(int(value)))
    val = ['0'] * (len(mask) - len(val)) + val
    for i in range(len(mask) - 1, -1, -1):
        if mask[i] in overrides:
            val[i] = mask[i]
    return ''.join(val)


def part1(data):
    mask_sets = [n for n in data.split('mask = ')]
    memory = {}
    for mask_set in mask_sets:
        if mask_set == '':
            continue
        lines = mask_set.splitlines()
        mask, records = lines[0], lines[1:]
        for record in records:
            address = int(record[record.index('[') + 1:record.index(']')])
            value = record.split(' = ')[1]
            result = int(eval_mask(mask, value, ('0', '1')), 2)
            memory[address] = result
    return sum(memory.values())


def collect_variations(value, variations):
    if 'X' not in value:
        variations.add(int(value, 2))
    else:
        collect_variations(value.replace('X', '1', 1), variations)
        collect_variations(value.replace('X', '0', 1), variations)


def part2(data):
    mask_sets = [n for n in data.split('mask = ')]
    memory = {}
    for mask_set in mask_sets:
        if mask_set == '':
            continue
        lines = mask_set.splitlines()
        mask, records = lines[0], lines[1:]
        for record in records:
            orig_address = int(record[record.index('[') + 1:record.index(']')])
            value = record.split(' = ')[1]
            masked_val = eval_mask(mask, orig_address, ('1', 'X'))
            addresses = set()
            collect_variations(masked_val, addresses)
            for a in addresses:
                memory[a] = int(value)
    return sum(memory.values())
