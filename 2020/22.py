from collections import deque
from itertools import islice


def play_crab_combat(p1, p2):
    if len(p1) == 0 or len(p2) == 0: # Game over
        if len(p1) > 0:
            return calculate_score(p1)
        else:
            return calculate_score(p2)
    p1_card, p2_card = p1.popleft(), p2.popleft()
    if p1_card > p2_card: # p1 wins round 
        p1.append(p1_card)
        p1.append(p2_card)
    else: # p2 wins round
        p2.append(p2_card)
        p2.append(p1_card)
    return play_crab_combat(p1, p2)

def play_recursive_combat(p1, p2):
    played = set()
    r = round
    while p1 and p2:
        if (tuple(p1), tuple(p2)) in played:
            return 1 # infinite game prevention
        played.add((tuple(p1), tuple(p2)))
        p1_card, p2_card = p1.popleft(), p2.popleft()
        
        round_winner = 0
        if len(p1) >= p1_card and len(p2) >= p2_card: # Recurse!
            round_winner = play_recursive_combat(deque(islice(p1.copy(), 0, p1_card)), deque(islice(p2.copy(), 0, p2_card)))
        elif p1_card > p2_card: # p1 wins round 
            round_winner = 1
        else: # p2 wins round
            round_winner = 2
            
        # Add winning cards
        if round_winner == 2:
            p2.append(p2_card)
            p2.append(p1_card)
        else:
            p1.append(p1_card)
            p1.append(p2_card)
    # Game over
    return 1 if p1 else 2
    
def calculate_score(deck):
    score = 0
    for i in range(len(deck)):
        score += deck[i] * (len(deck) - i)
    return score

def parse_decks(data):
    p1, p2 = data.split('\n\n')
    p1 = deque([int(n) for n in p1.splitlines()[1:]])
    p2 = deque([int(n) for n in p2.splitlines()[1:]])
    return p1, p2

def part1(data):
    p1, p2 = parse_decks(data)
    return play_crab_combat(p1, p2)

def part2(data):
    p1, p2 = parse_decks(data)
    winner = play_recursive_combat(p1, p2)
    if winner == 2:
        return calculate_score(p2)
    return calculate_score(p1)
