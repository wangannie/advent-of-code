
def part1(data):
    output_digits = [o.split(' | ')[1] for o in data.splitlines()]
    count = 0
    unique_lens = {2, 4, 3, 7}
    for line in output_digits:
        for digit in line.split():
            if len(digit) in unique_lens:
                count += 1
    return count

'''
Number of segments in s1 but not in s2
'''
def count_not_overlapping(s1, s2):
    count = 0
    for c in s1:
        if c not in s2:
            count += 1
    return count

def decode_line(line):
    inputs, outputs = line.split(' | ')
    inputs = inputs.split()
    outputs = outputs.split()
    num_to_code = {i: None for i in range(10)}
    
    code_lens = {}
    for s in inputs:
        code_lens[len(s)] = code_lens.get(len(s), []) + [s]
        
    # set digits that are unique by length
    num_to_code[1] = code_lens[2][0]
    num_to_code[4] = code_lens[4][0]
    num_to_code[7] = code_lens[3][0]
    num_to_code[8] = code_lens[7][0]
    
    for code in code_lens[6]:
        if count_not_overlapping(num_to_code[7], code) > 0:
            num_to_code[6] = code
        elif count_not_overlapping(num_to_code[4], code) > 0:
            num_to_code[0] = code
        else:
            num_to_code[9] = code
    
    for code in code_lens[5]:
        if count_not_overlapping(num_to_code[7], code) == 0:
            num_to_code[3] = code
        elif count_not_overlapping(num_to_code[6], code) == 1:
            num_to_code[5] = code
        else:
            num_to_code[2] = code
            
    code_to_num = dict((''.join(sorted(v)),k) for k,v in num_to_code.items())
    
    output_num = 0
    for digit in outputs:
        output_num = output_num * 10 + code_to_num[''.join(sorted(digit))]
    
    return output_num
        

def part2(data):
    lines = data.splitlines()
    output_sum = 0
    for line in lines:
        output_sum += decode_line(line)
    return output_sum
