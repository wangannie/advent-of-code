def count_diffs(nums):
    nums.sort()
    prev = 0
    ones, threes = 0, 0
    for i in range(len(nums)):
        diff = nums[i] - prev
        if diff == 1:
            ones += 1
        elif diff == 3:
            threes += 1
        prev = nums[i]
    return (ones, threes + 1)


def part1(data):
    nums = [int(n) for n in data.splitlines()]
    ones, threes = count_diffs(nums)
    return ones * threes


def part2(data):
    nums = [int(n) for n in data.splitlines()]
    nums.sort()
    dp = {}
    dp[0] = 1
    for i in range(len(nums)):
        dp[nums[i]] = dp.get(nums[i] - 1, 0) + dp.get(nums[i] - 2, 0) + dp.get(
            nums[i] - 3, 0)
    return dp[nums[-1]]
