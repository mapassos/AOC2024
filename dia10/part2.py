def main():

    with open('input.txt') as f:
        topo_map = [[int(height) for height in line] for line in f.read().splitlines()]

    count = 0
    for i in range(dim[0]):
        for j in range(dim[1]):
            height = 0
            if topo_map[i][j] == height:              
                search = Trailfinder(topo_map)
                count += search.count_trails(i, j, height)
    print(count)
    
class Trailfinder():
    def __init__(self, targetmap):
        self.targetmap = targetmap
        self.dim = (len(self.targetmap), len(self.targetmap[0]))
        self.directions = [
            (-1, 0),
            (0, 1),
            (1, 0),
            (0, -1)
        ]
        self.count = 0

    def count_trails(self, x, y,height):
        
        self.unique_peaks = []
        self.possible_trails(x, y, height)
        return self.count
        

    def possible_trails(self, x, y, height):
        if height < 9:
            height += 1
            for pos_dir in self.directions:
                xnew = x + pos_dir[0]
                ynew = y + pos_dir[1]
                if 0 <= xnew < self.dim[0] and 0 <= ynew < self.dim[1]:
                    if self.targetmap[xnew][ynew] == height:
                        self.possible_trails(xnew, ynew, height)
        else:
            self.count += 1
            return 
        return 
            

if __name__ == '__main__':
    main()
