def check_overlap(assignments, overlap_fn):
    e1, e2 = assignments.split(",")
    start1, end1 = map(int, e1.split("-"))
    start2, end2 = map(int, e2.split("-"))
    return overlap_fn(start1, end1, start2, end2)
    
def fully_contained(start1, end1, start2, end2):
    if (start1 <= start2 <= end1) and (start1 <= end2 <= end1):
        return True
    elif (start2 <= start1 <= end2) and (start2 <= end1 <= end2):
        return True
    return False

def part1(data):
    rows = data.splitlines()
    contained_count = 0
    for row in rows:
        contained_count += check_overlap(row, fully_contained)
    return contained_count

def overlapping(start1, end1, start2, end2):
    if (start1 <= start2 <= end1) or (start1 <= end2 <= end1):
        return True
    elif (start2 <= start1 <= end2) or (start2 <= end1 <= end2):
        return True
    return False
    
def part2(data):
    rows = data.splitlines()
    overlap_count = 0
    for row in rows:
        overlap_count += check_overlap(row, overlapping)
    return overlap_count


