def construct_map(lines):
    cave_system = {}
    for line in lines:
        v1, v2 = line.split('-')
        if v1 in cave_system:
            cave_system[v1].append(v2)
        else:
            cave_system[v1] = [v2]
        if v2 in cave_system:
            cave_system[v2].append(v1)
        else:
            cave_system[v2] = [v1]
    return cave_system

    
def find_distinct_paths(cave_system, double_visit_allowed):
    distinct_paths = []
    dfs(cave_system, distinct_paths, ['start'], not double_visit_allowed)
    return distinct_paths


def dfs(cave_system, paths, curr_path, double_small_used):
    curr = curr_path[-1]
    if curr == 'end':
        paths.append(curr_path)
        return
    for neighbor in cave_system[curr]:
        if neighbor.islower():
            if neighbor == 'start':
                continue
            if neighbor not in curr_path:
                dfs(cave_system, paths, curr_path + [neighbor], double_small_used)
            elif not double_small_used:
                dfs(cave_system, paths, curr_path + [neighbor], True)             
        else:
            dfs(cave_system, paths, curr_path + [neighbor], double_small_used)


def part1(data):
    lines = data.splitlines()
    return len(find_distinct_paths(construct_map(lines), False))
    

def part2(data):
    lines = data.splitlines()
    return len(find_distinct_paths(construct_map(lines), True))
