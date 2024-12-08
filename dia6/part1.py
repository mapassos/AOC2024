def main():

    with open('test.txt') as f:
        guard_map = [[pos for pos in line] for line in f.read().splitlines()]


    dim = (len(guard_map), len(guard_map[0]))
    guard_pos, obs_pos = get_positions(guard_map, dim)
    guard_path = set()
    guard_dir = (-1, 0)

    while not any(guard_pos[i] > dim[i] - 1 or guard_pos[i] <= 0 for i in range(2)):
        guard_path.add(guard_pos)
        guard_pos, guard_dir = guard_nextmov(obs_pos, guard_pos, guard_dir)
        
        
    print(len(guard_path))
        
def guard_nextmov(obstacle_pos, curr_pos, curr_dir):
    xnew = curr_pos[0] + curr_dir[0]
    ynew = curr_pos[1] + curr_dir[1]
    next_pos = (xnew, ynew)

    if next_pos in obstacle_pos:
        new_dir = obstruction_turn(curr_dir)
        return curr_pos, new_dir
    else:
        return next_pos, curr_dir    


def get_positions(target_map, dim):
    obstables_pos = []
    guard_pos = 0
    for i in range(dim[0]):
        for j in range(dim[1]):
            if target_map[i][j] == '#':
                obstables_pos.append((i, j))
            elif target_map[i][j] == '^':
                guard_pos = (i ,j)
    return guard_pos, obstables_pos
            

def obstruction_turn(curr_dir):
    # first direction is up, next is to the right of the last direction
    possible_dir = [
        (-1, 0),
        (0, 1),
        (1, 0),
        (0, -1)
        ]
    curr_idx = possible_dir.index(curr_dir)
    if curr_idx != len(possible_dir) - 1:
        nxt_dir = possible_dir[curr_idx + 1]
    else:
        nxt_dir = possible_dir[0]
    return nxt_dir

if __name__ == '__main__':
    main()
