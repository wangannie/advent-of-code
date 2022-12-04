# === BEGIN SHARED HELPERS ===
def total_points(rounds, find_score_fn):
    total_score = 0
    for r in rounds:
        s = find_score_fn(r)
        
        total_score += s
    return total_score

def get_shape_score(move):
    if ord(move) >= ord("X"):
        return ord(move) - ord("X") + 1
    return ord(move) - ord("A") + 1
    
def is_rock(move):
    return move == "A" or move == "X"

def is_paper(move):
    return move == "B" or move == "Y"

def is_scissors(move):
    return move == "C" or move == "Z"

# === END SHARED HELPERS === 

def find_score(round):
    opponent, me = round.split(" ")
    shape_score = get_shape_score(me)
    round_outcome_score = 0
    
    # normalize the moves
    if ord(opponent) == ord(me) - 23:
        # 3 points for a draw
        round_outcome_score = 3 
    elif (is_rock(opponent) and is_paper(me)) or \
        (is_paper(opponent) and is_scissors(me)) or \
            (is_scissors(opponent) and is_rock(me)):
        # 6 points for a win
        round_outcome_score = 6
        
    return shape_score + round_outcome_score

def part1(data):
    rounds = data.splitlines()
    return total_points(rounds, find_score)

def get_move_for_outcome(opponent, outcome):
    if outcome == "Z": # win
        if is_rock(opponent):
            return "B"
        elif is_paper(opponent):
            return "C"
        else:
            return "A"
    elif outcome == "X": # lose
        if is_rock(opponent):
            return "C"
        elif is_paper(opponent):
            return "A"
        else:
            return "B"
    else: # draw
        return opponent
    
def find_score2(round):
    opponent, outcome = round.split(" ")
    me = get_move_for_outcome(opponent, outcome)
    shape_score = get_shape_score(me)
    round_outcome_score = 0
    if outcome == "Z": # win
        round_outcome_score = 6
    elif outcome == "Y": # lose
        round_outcome_score = 3
    return shape_score + round_outcome_score

def part2(data):
    rounds = data.splitlines()
    return total_points(rounds, find_score2)
    
