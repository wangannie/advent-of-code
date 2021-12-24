import itertools
from collections import defaultdict
from copy import deepcopy


def apply_enhancement(img_dict, output_dict, alg, x_range, y_range):
    for x in range(x_range[0] - 1, x_range[1] + 2):
        for y in range(y_range[0] - 1, y_range[1] + 2):
            bitstring = ""
            for dy, dx in itertools.product(range(-1, 2), repeat=2):
                bitstring += str(img_dict[(x+dx, y+dy)])
            code = int(bitstring, 2)
            output_dict[(x, y)] = int(alg[code] == '#')
    return output_dict


def enhance(data, rounds):
    alg, input_img = data.split('\n\n')
    alg = list(alg)
    input_img = input_img.splitlines()
    img_dict = defaultdict()
    for y in range(len(input_img)):
        for x in range(len(input_img[0])):
            if input_img[y][x] == '#': img_dict[(x,y)] = 1
    x_range = (0, len(input_img[0]) - 1)
    y_range = (0, len(input_img) - 1)
    for i in range(rounds):
        x_range = (x_range[0] - i, x_range[1] + i)
        y_range = (y_range[0] - i, y_range[1] + i)
        img_dict = defaultdict(lambda: i % 2 if alg[0] == '#' else 0, img_dict)
        img_dict = apply_enhancement(deepcopy(img_dict), img_dict, alg, x_range, y_range)
    return sum([g for g in img_dict.values()])
    
    
def part1(data):
    return enhance(data, 2)
    
    
def part2(data):
    return enhance(data, 50)
