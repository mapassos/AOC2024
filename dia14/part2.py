def main():
    with open('input.txt') as f:
        bots_states = [[vals.split('=')[-1] for vals in line.split()] for line in f.read().splitlines()]

    bots_states = [[coords.split(',') for coords in info] for info in bots_states]

    grid_dim = (103, 101)
    
    bots_fstate = []
    
    for t in range(10000):
        curr_state = []
        if t != 0:
            bots_states = bots_fstate
            bots_fstate = []

        for state in bots_states:

            pos, vel = state

            if t == 0:
                
                pos = [int(pos[i]) for i in range(1, -1, -1)]
                vel = [int(vel[i]) for i in range(1, -1, -1)]
                
            pos = update_state(*pos, *vel)        
            pos = updated_state(*pos, *vel, grid_dim)

            bots_fstate.append([pos, vel])
            curr_state.append(pos)

        quads = count_quads(curr_state, grid_dim)
        if len([quads[i] for i in range(len(quads)) for j in range(i +1, len(quads)) if quads[i] > quads[j] * 8 or quads[i] < quads[j] / 8]) > 0:
            print(t + 1, quads)
            print_state(curr_state, grid_dim)
        

def count_quads(curr_state, dim):
    fst_quad = 0
    sec_quad = 0
    trd_quad = 0
    fth_quad = 0

    for x, y in curr_state:
        if x < dim[0]//2:
            if y < dim[1]//2:
                fst_quad += 1
            elif y > dim[1]//2:
                sec_quad += 1
        if x > dim[0]//2:
            if y < dim[1]//2:
                trd_quad += 1
            elif y > dim[1]//2:
                fth_quad += 1
    return fst_quad, sec_quad, trd_quad, fth_quad
   
def print_state(target_state, grid_dim):
    grid = ''
    state = [i for i in target_state]
    for i in range(grid_dim[0]):
        for j in range(grid_dim[1]):
            if (i, j) in state:
                grid += '1'
                state.remove((i,j))
                while (i, j) in state:
                    grid = grid[:-1] + '2'
                    state.remove((i,j))
            else:
                grid += '.'
        grid += '\n'

    print(grid)
            

def update_state(x, y, vx, vy):
    x += vx
    y += vy

    return x, y


def updated_state(x, y, vx, vy, dim):
    if x >= 0:
        x %= dim[0]       
    elif x < 0:
        x = abs(x) % dim[0]
        if x != 0:
            x = dim[0] - x
        

    if y >= 0:
        y %= dim[1]
    elif y < 0:
        y = abs(y) % dim[1]
        if y != 0:
            y = dim[1] - y

    return x, y
        
        

if __name__ == '__main__':
    main()
