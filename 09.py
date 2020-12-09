pre_len = 25  # preamble length aka number of prev values to search for a sum


def two_sum(nums, target):
    needed = set()
    for n in nums:
        if n in needed:
            return True  # sum found
        needed.add(target - n)
    return False


def invalid_sum(nums):
    window = set()
    for i in range(pre_len):  # only add preamble to window
        window.add(nums[i])  # duplicates don't matter
    start, end = 0, pre_len - 1
    target = pre_len
    while end < len(nums):
        if not two_sum(window, nums[target]):
            return nums[target]
        # sum is valid, update window
        window.remove(nums[start])
        start += 1
        end += 1
        window.add(nums[end])
        target += 1


# Finds (start, end) indices for a contiguous subarray that sums to k
def subarray_sum(arr, k):
    prefix_sums = [0] * len(arr)
    prefix_sums[0] = arr[0]
    first = 0
    for i in range(1, len(arr)):
        curr_sum = prefix_sums[i - 1] + arr[i]
        while curr_sum > k and first < i - 1:
            curr_sum -= arr[first]
            first += 1
        if curr_sum == k:
            return (first, i)
        prefix_sums[i] = curr_sum


def part1(data):
    nums = [int(n) for n in data.splitlines()]
    return invalid_sum(nums)


def part2(data):
    nums = [int(n) for n in data.splitlines()]
    target = invalid_sum(nums)
    start, end = subarray_sum(nums, target)
    range_min = min(nums[start:end + 1])
    range_max = max(nums[start:end + 1])
    return range_min + range_max
