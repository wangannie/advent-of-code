import itertools
from collections import Counter


def dice_roll(dice_max):
    num = 1
    while True:
        if num > dice_max:
            num = 1
        yield num
        num += 1
        

def part1(data):
    starting_pos = [int(player.split(': ')[1]) for player in data.splitlines()]
    num_turns = 0
    p1_score, p2_score = 0, 0
    p1_pos, p2_pos = starting_pos
    pts_to_win = 1000
    p1_turn = True
    dice = dice_roll(100)
    while p1_score < pts_to_win and p2_score < pts_to_win:
        moves = 0
        for _ in range(3): 
            moves += next(dice)
        if p1_turn:
            p1_pos += moves
            p1_pos = 10 if p1_pos % 10 == 0 else p1_pos % 10
            p1_score += p1_pos
        else:
            p2_pos += moves
            p2_pos = 10 if p2_pos % 10 == 0 else p2_pos % 10
            p2_score += p2_pos
        num_turns += 1
        p1_turn = not p1_turn
    return min(p1_score, p2_score) * num_turns * 3


def run_game_turn(p1_pos, p1_score, p2_pos, p2_score, outcomes, pts_to_win, p1_turn, dice_combos):
    if not (p1_score < pts_to_win and p2_score < pts_to_win): return
    init_state = (p1_pos, p1_score, p2_pos, p2_score)
    init_state_count = outcomes[(p1_pos, p1_score, p2_pos, p2_score)]
    outcomes[(p1_pos, p1_score, p2_pos, p2_score)] = 0
    for moves, cnt in dice_combos.items():
        p1_pos, p1_score, p2_pos, p2_score = init_state
        if p1_turn:
            p1_pos += moves
            p1_pos = 10 if p1_pos % 10 == 0 else p1_pos % 10
            p1_score += p1_pos
        else:
            p2_pos += moves
            p2_pos = 10 if p2_pos % 10 == 0 else p2_pos % 10
            p2_score += p2_pos
        outcomes[(p1_pos, p1_score, p2_pos, p2_score)] = outcomes.get((p1_pos, p1_score, p2_pos, p2_score), 0) + cnt * init_state_count
        run_game_turn(p1_pos, p1_score, p2_pos, p2_score, outcomes, pts_to_win, not p1_turn, dice_combos)


def count_winning_outcomes(outcomes, pts_to_win):
    p1_wins, p2_wins = 0, 0
    for state, count in outcomes.items():
        _, p1_score, _, p2_score = state
        if p1_score >= pts_to_win:
            p1_wins += count
        elif p2_score >= pts_to_win:
            p2_wins += count
    return p1_wins, p2_wins

    
def part2(data):
    starting_pos = [int(player.split(': ')[1]) for player in data.splitlines()]
    p1_score, p2_score = 0, 0
    p1_pos, p2_pos = starting_pos
    pts_to_win = 21
    outcomes = {(p1_pos, p1_score, p2_pos, p2_score): 1}
    dice_combos = Counter([sum(roll) for roll in list(itertools.product(range(1,4),repeat=3))])
    run_game_turn(p1_pos, p1_score, p2_pos, p2_score, outcomes, pts_to_win, True, dice_combos)
    return max(count_winning_outcomes(outcomes, pts_to_win))
