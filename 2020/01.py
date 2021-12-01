def twoSumProduct(nums, target, start):
    needed = set()
    for i in range(start, len(nums)):
        if nums[i] in needed:
            return (target - nums[i]) * nums[i]
        needed.add(target - nums[i])
    return -1


def threeSumProduct(nums, target):
    for i in range(len(nums)):
        pair = twoSumProduct(nums, target - nums[i], i)
        if pair > -1:
            return pair * nums[i]
    return -1


def part1(data):
    nums = [int(n) for n in data.splitlines()]
    return twoSumProduct(sorted(nums), 2020, 0)


def part2(data):
    nums = [int(n) for n in data.splitlines()]
    return threeSumProduct(sorted(nums), 2020)
