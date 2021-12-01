def count_increases(nums):
    increases = 0
    prev = nums[0]
    for i in range(1, len(nums)):
        if nums[i] > prev:
            increases += 1
        prev = nums[i]
    return increases

def get_window_sums(nums):
    window_sums = []
    m1, m2 = nums[0], nums[1]
    for i in range(2, len(nums)):
        window_sums.append(m1 + m2 + nums[i])
        m1 = m2
        m2 = nums[i]
    return window_sums


def part1(data):
    nums = [int(n) for n in data.splitlines()]
    return count_increases(nums)


def part2(data):
    nums = [int(n) for n in data.splitlines()]
    return count_increases(get_window_sums(nums))
