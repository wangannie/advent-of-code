def find_loop_size(secret_key):
    subject_num = 7
    value = 1
    loops = 0
    while value != secret_key:
        value *= subject_num
        value = value % 20201227
        loops += 1
    return loops
    
def decrypt_key(subject_num, loop_size):
    value = 1
    for i in range(loop_size):
        value *= subject_num
        value = value % 20201227
    return value

def part1(data):
    card_public, door_public = [int(n) for n in data.splitlines() ]
    card_loop = find_loop_size(card_public)
    door_loop = find_loop_size(door_public)
    encryption_key = decrypt_key(door_public, card_loop)
    if encryption_key == decrypt_key(card_public, door_loop):
        return encryption_key
    print("Encryption key mismatch!")
    
    