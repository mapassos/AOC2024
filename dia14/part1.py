def main():
    with open('input.txt') as f:
        bots_states = [[vals.split('=')[-1] for vals in line.split()] for line in f.read().splitlines()]

    bots_states = [[coords.split(',') for coords in info] for info in bots_states]

    grid_dim = (103, 101)
    bots_fstate = []
    for state in bots_states:
        pos, vel = state

        botstate = SecBotState(*pos[::-1], *vel[::-1])
        for _ in range(100):
            botstate.evolve_state()

        botstate.final_state()
        bots_fstate.append((botstate.x, botstate.y))

    fst_quad = 0
    sec_quad = 0
    trd_quad = 0
    fth_quad = 0

    for x, y in bots_fstate:
        if x < grid_dim[0]//2:
            if y < grid_dim[1]//2:
                fst_quad += 1
            elif y > grid_dim[1]//2:
                sec_quad += 1
        if x > grid_dim[0]//2:
            if y < grid_dim[1]//2:
                trd_quad += 1
            elif y > grid_dim[1]//2:
                fth_quad += 1
                
    print_state(bots_fstate)

    print(fst_quad * sec_quad * trd_quad * fth_quad)
            
def print_state(target_state):
    grid = ''
    state = [i for i in target_state]
    for i in range(7):
        for j in range(11):
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
            


class SecBotState():
    grid_dim = (103, 101)
    state = []

    def __init__(self, posx, posy, vx, vy):
        self.x = int(posx)
        self.y = int(posy)
        self.vx = int(vx)
        self.vy = int(vy)
        SecBotState.state.append(self)

    def evolve_state(self):
        self.x += self.vx
        self.y += self.vy

    def final_state(self):
        if self.x >= 0:
            self.x %= self.grid_dim[0]
            
        elif self.x < 0:
            self.x = abs(self.x) % self.grid_dim[0]
            if self.x != 0:
                self.x = self.grid_dim[0] - self.x
            

        if self.y >= 0:
            self.y %= self.grid_dim[1]
        elif self.y < 0:
            self.y = abs(self.y) % self.grid_dim[1]
            if self.y != 0:
                self.y = self.grid_dim[1] - self.y
 
    
        

if __name__ == '__main__':
    main()
