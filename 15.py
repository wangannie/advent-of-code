from collections import deque


def update_history(history, val, turn):
    hist = history.get(val, deque([]))
    hist.append(turn)
    if len(hist) > 2:
        hist.popleft()
    history[val] = hist


def start_game(starting_nums, total_turns):
    history = {}
    turn = 1
    while turn <= len(starting_nums):
        history[starting_nums[turn - 1]] = deque([turn])
        turn += 1
    prev_num = starting_nums[-1]
    while turn <= total_turns:
        result = 0
        if prev_num in history and len(history[prev_num]) > 1:
            result = history[prev_num][1] - history[prev_num][0]
        update_history(history, result, turn)
        prev_num = result
        turn += 1
    return prev_num


def part1(data):
    starting_nums = [int(n) for n in data.split(',')]
    return start_game(starting_nums, 2020)


def part2(data):
    starting_nums = [int(n) for n in data.split(',')]
    return start_game(starting_nums, 30000000)
