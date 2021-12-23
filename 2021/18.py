import itertools


def process_line(line):
    unpaired_depths = set()
    nums = []
    depth = 0
    for c in line:
        if c == ',':
            continue
        elif c == '[':
            depth += 1
            unpaired_depths.add(depth)
        elif c == ']':
            depth -= 1
            if depth in unpaired_depths:
                unpaired_depths.remove(depth)
        else:
            if depth in unpaired_depths:
                nums.append((int(c), depth, 'L'))
                unpaired_depths.remove(depth)
            else:
                nums.append((int(c), depth, 'R'))
    return nums


def reduce(nums):
    changed = False
    for i in range(len(nums) - 1):
        if nums[i][1] > 4 and nums[i+1][1] == nums[i][1]: # pair of depth > 4
            explode(nums, i)
            changed = True
            break
    if not changed:
        for i in range(len(nums)):
            if nums[i][0] >= 10:
                split(nums, i)
                changed = True
                break
    if changed:
        reduce(nums)
        
            
def explode(nums, start_index):
    p1, p2 = nums[start_index], nums[start_index + 1]
    if start_index > 0: # not at the very end
        orig_val, orig_depth, _ = nums[start_index - 1]
        nums[start_index - 1] = (orig_val + p1[0], orig_depth, nums[start_index-1][2])
    if start_index + 2 < len(nums): # not at very end
        orig_val, orig_depth, _= nums[start_index + 2]
        nums[start_index + 2] = (orig_val + p2[0], orig_depth, nums[start_index + 2][2])
    if start_index > 0 and nums[start_index - 1][1] == nums[start_index][1] - 1 and nums[start_index - 1][2] == 'L':
        nums[start_index] = (0, nums[start_index][1] - 1, 'R')
    elif start_index + 2 < len(nums) and nums[start_index + 2][1] == nums[start_index][1] - 1 and nums[start_index + 2][2] == 'R':
        nums[start_index] = (0, nums[start_index][1] - 1, 'L')
    else:
        nums[start_index] = (0, nums[start_index][1] - 1, nums[start_index][2])
    nums.pop(start_index + 1) # remove the second in the pair


def split(nums, index):
    orig_val, orig_depth, _ = nums[index]
    n1 = orig_val // 2
    n2 = orig_val - n1
    nums[index] = (n1, orig_depth + 1, 'L')
    nums.insert(index + 1, (n2, orig_depth + 1, 'R'))
    
    
def add_lines(n1, n2):
    return [(val, depth + 1, side) for val, depth, side in n1 + n2]


def find_magnitude(nums):
    total = 0
    while len(nums) > 1:
        for i in range(len(nums) - 1):
            if nums[i+1][1] == nums[i][1]: # pair of equal depth
                mag = 3 * nums[i][0] + 2 * nums[i+1][0]
                nums[i] = (mag, nums[i][1] - 1, 'R')
                nums.pop(i+1)
                break
    total = nums[0][0]
    return total
    
    
def part1(data):
    lines = [process_line(line) for line in data.splitlines()]
    curr = lines[0]
    for i in range(1, len(lines)):
        curr = add_lines(curr, lines[i])
        reduce(curr)
    return find_magnitude(curr)

    
def part2(data):
    lines = [process_line(line) for line in data.splitlines()]
    max_magnitude = 0
    for i, j in itertools.combinations(range(len(lines)), 2):
        added = add_lines(lines[i], lines[j])
        reduce(added)
        max_magnitude = max(find_magnitude(added), max_magnitude)
        
        # add in both directions
        added = add_lines(lines[j], lines[i])
        reduce(added)
        max_magnitude = max(find_magnitude(added), max_magnitude)
    return max_magnitude


# ====== extra helper stuff for testing ======

# (very unnecessary and complicated) function to convert the parsed snailfish
# number back to a string format
def format_to_str(nums):
    res = ''
    curr_depth = 0
    depth_status = {}
    # Depth status codes:
    # 0, open left bracket
    # 1, left part of pair done
    # 2, right part sealed aka pair complete
    
    for i in range(len(nums)):
        val, depth, side = nums[i]
        while curr_depth < depth:
            res += '['
            curr_depth += 1
            depth_status[curr_depth] = 0 # opened left 
        if curr_depth > 0 and (curr_depth not in depth_status or depth_status[curr_depth] == 2):
            res += '['
            depth_status[curr_depth] = 0 # opened left
        res += str(val) # append value
        if side == 'L':
            res += ','
            depth_status[curr_depth] = 1 # left of pair is done
        else:
            res += ']'
            depth_status[curr_depth] = 2 # completed pair at curr_depth
            i = 1
            while curr_depth - i > 0 and curr_depth - i in depth_status and depth_status[curr_depth - i] == 1:
                res += ']'
                depth_status[curr_depth - i] = 2
                i += 1
            if curr_depth - i > 0 and curr_depth - i in depth_status and depth_status[curr_depth - i] == 0:
                res += ','
                depth_status[curr_depth - i] = 1
            curr_depth = curr_depth - i
    return res

def tests():
    print("== ⏯️ ex 1: parsing and reduce sanity ==")
    input = "[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]"
    nums = process_line(input)
    parsed = format_to_str(nums)
    assert parsed == input, ("parsing got", parsed, "but expected", input)
    reduce(nums)
    res = format_to_str(nums)
    assert res == "[[3,[2,[8,0]]],[9,[5,[7,0]]]]", ("reduce got: ", res)
    print("... ok ✅ passed ex 1 parsing sanity==\n\n")
    
    print("== ⏯️ ex 2 addition sanity ==")
    in_1 = "[[[[4,3],4],4],[7,[[8,4],9]]]"
    in_2 = "[1,1]"
    nums_1 = process_line(in_1)
    nums_2 = process_line(in_2)
    nums = add_lines(nums_1, nums_2)
    formatted = format_to_str(nums)
    assert formatted == "[[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]", ("adding and parsing got", formatted, "but expected", "[[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]")
    reduce(nums)
    res = format_to_str(nums)
    assert res == "[[[[0,7],4],[[7,8],[6,0]]],[8,1]]", ("reduce got: ", res)
    print("... ok ✅ passed ex 2 ==\n\n")

    print("== ⏯️ ex 3 paired nesting parsing ==")
    input = "[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]"
    nums = process_line(input)
    formatted = format_to_str(nums)
    assert formatted == input, ("Failed: got", formatted, "but expected:", input)
    print("... ok ✅ passed ex 3 parsing ==\n\n")
    
    print("== ⏯️ ex 4 explosion sanity ==")
    input = "[[6,[5,[4,[3,2]]]],1]"
    expected = "[[6,[5,[7,0]]],3]"
    nums = process_line(input)
    reduce(nums)
    res = format_to_str(nums)
    assert res == expected, ("expected: ", expected)
    print("... ok ✅ passed ex 4 explosion sanity ==\n\n")
    
    print("== ⏯️ ex 5 reduce with addition ==")
    ex5_1 = "[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]"
    ex5_2 = "[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]"
    nums_1 = process_line(ex5_1)
    nums_2 = process_line(ex5_2)
    nums = add_lines(nums_1, nums_2)
    formatted = format_to_str(nums)
    assert formatted == "[[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]],[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]]", ("expected: ", formatted)
    reduce(nums)
    res = format_to_str(nums)
    assert res == "[[[[4,0],[5,4]],[[7,7],[6,0]]],[[8,[7,7]],[[7,9],[5,0]]]]", ("expected: ", res)
    print("... ok ✅ passed ex 5 reduce with addition ==\n\n")
