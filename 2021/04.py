def parse_input(data):
    data = data.replace('  ', ' ').replace('\n ', '\n')
    sections = data.split('\n\n')
    order = list(map(int, sections[0].split(',')))
    boards = []
    for board in sections[1:]:
        boards.append(parse_board(board))
    return order, boards


def parse_board(board_str):
    board = []
    lines = board_str.split('\n')
    for l in lines:
        board.append(list(map(int, l.split(' '))))
    return board
    
    
def start_game_part_1(boards, order):
    for i in range(len(order)):
        for board in boards:
            mark_number(board, order[i])
            if check_winning_board(board):
                return find_winning_score(board, order[i])
            
            
def start_game_part_2(boards, order):
    boards_won = set()
    for i in range(len(order)):
        for b in range(len(boards)):
            if b in boards_won:
                continue
            mark_number(boards[b], order[i])
            if check_winning_board(boards[b]):
                if len(boards_won) == len(boards) - 1: # is the only remaining board
                    return find_winning_score(boards[b], order[i])
                boards_won.add(b)


def mark_number(board, number):
    for r in range(len(board)):
        for c in range(len(board)):
            if board[r][c] == number:
                board[r][c] = -1
        
        
def check_winning_board(board):
    for row in board:
        if sum(row) == -5: # all marked (set to -1)
            return True
    for i in range(5):
        if sum([board[r][i] for r in range(5)]) == -5:
            return True
    return False


def find_winning_score(board, just_called):
    unmarked_sum = 0
    for r in range(len(board)):
        for c in range(len(board)):
            if board[r][c] > -1:
                unmarked_sum += board[r][c]
    return unmarked_sum * just_called


def part1(data):
    order, boards = parse_input(data)
    return start_game_part_1(boards, order)


def part2(data):
    order, boards = parse_input(data)
    return start_game_part_2(boards, order)
