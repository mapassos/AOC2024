import argparse

def count_distinct_pos(area_map):

    def guard_nextmov(curr_pos, curr_dir):

        xnew = curr_pos[0] + DIRECTIONS[curr_dir][0]
        ynew = curr_pos[1] + DIRECTIONS[curr_dir][1]
        next_pos = (xnew, ynew)

        if next_pos in obs_pos:
            new_dir = (curr_dir + 1) % 4
            return curr_pos, new_dir
        else:
            return next_pos, curr_dir    


    def get_positions():
        obstables_pos = []
        guard_pos = 0
        for i in range(DIM[0]):
            for j in range(DIM[1]):
                if area_map[i][j] == '#':
                    obstables_pos.append((i, j))
                elif area_map[i][j] == '^':
                    guard_pos = (i ,j)
        return guard_pos, obstables_pos

    area_map = [[pos for pos in line] for line in area_map.splitlines()]
  
    DIM = (len(area_map), len(area_map[0]))
    guard_pos, obs_pos = get_positions()
    guard_path = set()

    DIRECTIONS = (
        (-1, 0),
        (0, 1),
        (1, 0),
        (0, -1)
    )

    guard_dir = 0

    while not any(guard_pos[i] > DIM[i] - 1 or guard_pos[i] <= 0 for i in range(2)):
        guard_path.add(guard_pos)
        guard_pos, guard_dir = guard_nextmov(guard_pos, guard_dir)
        
    return len(guard_path)   
        

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-f', '--file',
        default = 'test.txt',
        help = 'Name of the file'
    )

    args = parser.parse_args()
 
    with open(args.file) as f:
        area_map = f.read()

    print(count_distinct_pos(area_map))

if __name__ == '__main__':
    main()
