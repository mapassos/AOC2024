def main():
    with open('input.txt') as f:
        warehouse = [line for line in f.read().split('\n\n')]

    warehouse, actions = warehouse[0], warehouse[1]
    warehouse = [[col for col in line] for line in warehouse.splitlines()]
    actions = [act for line in actions.splitlines() for act in line]

    dim = (len(warehouse), len(warehouse[0]))

    map_pos = {'#': list()}

    for i in range(dim[0]):
        for j in range(dim[1]):
            if warehouse[i][j] == '#':
                map_pos['#'].append((i, j))
            elif warehouse[i][j] == '@':
                map_pos['@'] = (i, j)

    directions = {
        '>' : (0,1),
        'v' : (1,0),
        '<' : (0,-1),
        '^' : (-1,0)
    }

                
    bot_pos = map_pos.get('@')
    #print('\n'.join(''.join(line) for line in warehouse))

    while actions:
        
        d = directions[actions[0]]
        xnew = bot_pos[0] + d[0]
        ynew = bot_pos[1] + d[1]
        
        if (xnew, ynew) not in map_pos.get('#'):
            if warehouse[xnew][ynew] == 'O':
                while warehouse[xnew][ynew] == 'O':
                    xnew += d[0]
                    ynew += d[1]
                if (xnew, ynew) not in map_pos.get('#'):
                    while (xnew, ynew) != bot_pos:
                        warehouse[xnew][ynew] = 'O'
                        xnew -= d[0]
                        ynew -= d[1]
                    warehouse[bot_pos[0]][bot_pos[1]] = '.'
                    bot_pos = (
                        bot_pos[0] + d[0],
                        bot_pos[1] + d[1]
                        )
                    warehouse[bot_pos[0]][bot_pos[1]] = '@'
                    del actions[0]
                else:
                    del actions[0]
            else:
                warehouse[bot_pos[0]][bot_pos[1]] = '.'
                bot_pos = (xnew, ynew)
                warehouse[bot_pos[0]][bot_pos[1]] = '@'
                del actions[0]
        else:
            del actions[0]

    #print('\n'.join(''.join(line) for line in warehouse))

    res = 0
    for i in range(dim[0]):
        for j in range(dim[1]):
            if warehouse[i][j] == 'O':
                res += 100 * i + j

    print(res)

if __name__ == '__main__':
    main()
