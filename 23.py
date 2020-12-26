# -------- Linked List Version --------

class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next
    def __str__(self):
        return f"{self.val}"
        
# Pretty-print linked list for debugging
def print_list(head):
    result = str(head.val) + " > "
    first = head.val
    head = head.next
    loop = False
    while head.val != first:
        result += str(head) + " > "
        head = head.next
    print(result)

def construct_linked_list(cups, nodes, max_node):
    sentinel = Node(-1)
    prev = sentinel
    for c in cups:
        nodes[c] = Node(c)
        prev.next = nodes[c]
        prev = nodes[c]
    for i in range(max(cups) + 1, max_node + 1):
        nodes[i] = Node(i)
        prev.next = nodes[i]
        prev = nodes[i]
    prev.next = sentinel.next
    return sentinel

def play_game(sentinel, rounds, nodes, max_node):
    current = sentinel.next
    for i in range(rounds):
        pick1 = current.next
        pick2 = pick1.next
        pick3 = pick2.next
        picked = [pick1, pick2, pick3]
        current.next = pick3.next # remove 3 cups
        dest = current.val - 1
        while dest == 0 or nodes[dest] in picked:
            dest -= 1
            if dest < 1:
                dest = max_node
        dest_node = nodes[dest]
        temp = dest_node.next
        for p in picked:
            dest_node.next = p
            dest_node = dest_node.next
        dest_node.next = temp
        current = current.next

def part1(data):
    cups = [int(n) for n in list(data)]
    nodes = {}
    sentinel = construct_linked_list(cups, nodes, max(cups))
    play_game(sentinel, 100, nodes, max(cups))
    
    # Construct result string
    curr = nodes[1].next
    result = ""
    while curr.val != 1:
        result += str(curr.val)
        curr = curr.next
    return result

def part2(data):
    cups = [int(n) for n in list(data)]
    nodes = {}
    sentinel = construct_linked_list(cups, nodes, 1000000)
    play_game(sentinel, 10000000, nodes, 1000000)
    return nodes[1].next.val * nodes[1].next.next.val


# -------- First array-based solution for Part 1 --------
def find_dest_index(cups, current):
    possible = sorted(cups[:current] + cups[current + 1:])
    max_dest, min_dest = max(possible), min(possible)
    check = cups[current] - 1
    while True:
        if check < min_dest:
            check = max_dest
        if check in possible:
            return cups.index(check)
        else:
            check -= 1
        
def insert_list(cups, pickup, dest):
    cups = cups[:dest + 1] + pickup + cups[dest + 1:]
    return cups
        
def move(cups, current, num):
    current = current % len(cups)
    current_cup = cups[current]
    start, end = (current + 1) % len(cups), (current + 4) % len(cups)
    if start > end:
        pickup = cups[start:] + cups[:end]
        del cups[start:]
        del cups[:end]
    else:
        pickup = cups[start:end]
        del cups[start:end]
    dest_index = find_dest_index(cups, cups.index(current_cup))
    cups = insert_list(cups, pickup, dest_index)
    return cups, cups.index(current_cup) + 1

def find_result_arr(cups):
    root = cups.index(1)
    result = cups[root + 1:] + cups[:root]
    return ''.join([str(r) for r in result])

def part1_arr(data):
    cups = [int(n) for n in list(data)]
    current = 0
    for i in range(1, 101):
        cups, current = move(cups, current, i)
    return find_result_arr(cups)
