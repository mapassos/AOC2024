from collections import defaultdict

def main():

    with open('input.txt') as f:
        ant_map = f.read().splitlines()

    ant_map = [[pos for pos in line] for line in ant_map]

    ants = defaultdict(list)
    dim = (len(ant_map), len(ant_map[0]))

    #get all the positions of each type of antenna
    for i in range(dim[0]):
        for j in range(dim[0]):
            if ant_map[i][j] != '.':
                ants[ant_map[i][j]].append((i,j))

    for ant in ants:
        num_ant = len(ants[ant])
        
        for i, coord1 in enumerate(ants[ant]):
            for j in range(i + 1,num_ant):
                coord2 = ants[ant][j]
                
                xcoord1, ycoord1 = coord1[0], coord1[1]
                xcoord2, ycoord2 = coord2[0], coord2[1]
                
                xdif = xcoord1 -  xcoord2
                ydif = ycoord1 -  ycoord2
                
                node_xcoord = coord1[0] + xdif
                node_ycoord = coord1[1] + ydif
                

                if 0 <= node_xcoord < dim[0] and 0 <= node_ycoord < dim[1]:
                    
                    if ant_map[node_xcoord][node_ycoord] != '#':
                        ant_map[node_xcoord][node_ycoord] =  '#'
                        
                node_xcoord = coord2[0] - xdif
                node_ycoord = coord2[1] - ydif

                if 0 <= node_xcoord < dim[0] and 0 <= node_ycoord < dim[1]:
                    if ant_map[node_xcoord][node_ycoord] != '#':
                        ant_map[node_xcoord][node_ycoord] =  '#'
                        

    print(('\n').join(('').join(ant_map[i]) for i in range(dim[1])))
    print(sum(i.count('#') for i in ant_map))
        

if __name__ ==  '__main__':
    main()
