import math

operators = {
    0: sum,
    1: math.prod,
    2: min,
    3: max,
    5: lambda a, b: int(a > b),
    6: lambda a, b: int(a < b),
    7: lambda a, b: int(a == b),
}


# source: https://stackoverflow.com/questions/1425493/convert-hex-to-binary
def hex_to_binary(input):
    num_of_bits = len(input) * 4
    return bin(int(input, 16))[2:].zfill(num_of_bits)

    
def process_packets(input):
    ver_code = int(input[:3], 2)
    type_code = int(input[3:6], 2)
    if type_code == 4: # literal type
        literal = ""
        for i in range(6, len(input), 5):
            curr_chunk = input[i: i + 5]
            literal += curr_chunk[1:]
            if curr_chunk[0] == '0':
                break
        packet_len = 6 + len(literal) // 4 + len(literal)
        return ver_code, int(literal, 2), packet_len
    else:
        op_mode = input[6]
        ver_code_sum = ver_code
        start_index = 0
        args = []
        if op_mode == '0': # next 15 bits are the length of the subpackets
            subpackets_len = int(input[7:22], 2)
            start_index = 22
            while start_index < subpackets_len + 22:
                sub_ver_code_sum, subpacket_val, packet_len = process_packets(input[start_index:])
                args.append(subpacket_val)
                ver_code_sum += sub_ver_code_sum
                start_index += packet_len
        else: # next 11 bits represent the number of subpackets
            num_subpackets = int(input[7:18], 2)
            start_index = 18
            for _ in range(num_subpackets):
                sub_ver_code_sum, subpacket_val, packet_len = process_packets(input[start_index:])
                ver_code_sum += sub_ver_code_sum
                args.append(subpacket_val)
                start_index += packet_len
        
        # execute operations
        op_func = operators[type_code]
        if type_code < 4:
            result = op_func(args)
            return ver_code_sum, result, start_index
        else:
            result = op_func(args[0], args[1])
            return ver_code_sum, result, start_index
    
    
def part1(data):
    bin = hex_to_binary(data)
    return process_packets(bin)[0]


def part2(data):
    bin = hex_to_binary(data)
    return process_packets(bin)[1]
