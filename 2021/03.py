def get_rates(bit_strings):
    all_f = int('1' * len(bit_strings[0]), 2)
    midpoint = len(bit_strings) // 2 - 1
    gamma_str = ""
    for i in range(len(bit_strings[0])):
        gamma_str += sorted(bit_strings, key=lambda x: x[i])[midpoint][i]
    gamma_rate = int(gamma_str, 2)
    epsilon_rate = ~gamma_rate & all_f
    return gamma_rate * epsilon_rate


def get_bit_count(bit_strings, bit_index):
    one_count = 0
    for bit_str in bit_strings:
        one_count += int(bit_str[bit_index])
    return one_count
        
        
def filter_by_bit(bit_strings, bit_index, match_bit):
    return list(filter(lambda x: int(x[bit_index]) == match_bit, bit_strings))


# most_common = True for oxygen generator rating, False otherwise
def get_rating(bit_strings, most_common):
    bit_index = 0
    while len(bit_strings) > 1:
        if get_bit_count(bit_strings, bit_index) >= len(bit_strings) / 2:
            bit_strings = filter_by_bit(bit_strings, bit_index, int(most_common))
        else:
            bit_strings = filter_by_bit(bit_strings, bit_index, int(not most_common))
        bit_index += 1
    return int(bit_strings[0], 2)
    
    
def part1(data):
    bit_strings = [n for n in data.splitlines()]
    return get_rates(bit_strings)


def part2(data):
    nums = [n for n in data.splitlines()]
    return get_rating(list(nums), True) * get_rating(list(nums), False)

