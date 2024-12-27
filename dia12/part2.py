import time

def main():

    with open('test.txt') as f:
        garden = f.read().splitlines()

    dim = (len(garden), len(garden[0]))

    directions = (
        (0,1),
        (1,0),
        (0,-1),
        (-1,0)
    )

    pgroups = []
    outbounds_group = []
    seen_path = set()
    for i in range(dim[0]):
        for j in range(dim[1]):
            if (i, j) not in seen_path:
                path = set()
                #we are getting all the squares that borders each square we have seen
                #and the directions which we arrive into them
                outbounds = []
                pgroups.append(search_groups(garden, dim, garden[i][j], i, j, directions, path, outbounds))
                seen_path.update(pgroups[-1])
                outbounds_group.append(outbounds)
    
    res = 0

    #to obtain the number of sides we look to the perpendicular direction of the
    #directions we have collected and when that side does not contain any square from the border,
    #that means we have a side of the shape
    for outbounds, group in zip(outbounds_group, pgroups):
        sides = 0
        for x, y, d in set(outbounds):
            if (x + directions[d][1], y + directions[d][0], d) not in outbounds:
                sides += 1
        res += sides * len(group)
        
    print(res)

def search_groups(garden, dim, target_plant, x, y, directions, path, outbounds):

    path.add((x,y))
    
    for d, (dx, dy) in enumerate(directions):
        
        xnew = x + dx
        ynew = y + dy
        
        if (xnew, ynew) not in path and 0 <= xnew < dim[0] and 0 <= ynew < dim[1] and garden[xnew][ynew] == target_plant:
            path.update(search_groups(garden, dim, target_plant, xnew, ynew, directions, path, outbounds))
        else:
            if (xnew, ynew) not in path:
                outbounds.append((xnew, ynew, d))

    return path

                
if __name__ == '__main__':
    mean = []
    for i in range(50):
        t = time.time()
        main()
        mean.append(time.time() - t)

    print(sum(mean)/len(mean))
