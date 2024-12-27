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
    seen_path = set()
    for i in range(dim[0]):
        for j in range(dim[1]):
            if (i, j) not in seen_path:
                path = set()
                pgroups.append(search_groups(garden, dim, garden[i][j], i, j, directions, path))
                seen_path.update(pgroups[-1])

    res = 0
    for group in pgroups:
        perimeter = 0
        for x, y in group:
            for dx, dy in directions:
                if (x + dx, y + dy) not in group:
                    perimeter += 1
        res += len(group) * perimeter

    print(res)
    

def search_groups(garden, dim, target_plant, x, y, directions, path):

    path.add((x,y))
    
    for pdir in directions:
        
        xnew = x + pdir[0]
        ynew = y + pdir[1]
        
        if (xnew, ynew) not in path and 0 <= xnew < dim[0] and 0 <= ynew < dim[1] and garden[xnew][ynew] == target_plant:
            path.update(search_groups(garden, dim, target_plant, xnew, ynew, directions, path))

    return path

                
if __name__ == '__main__':
    main()
