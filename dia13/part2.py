import re
import numpy as np

def main():
    with open('input.txt') as f:
        machines = [[buttons for buttons in machine.splitlines()] for machine in f.read().split('\n\n')]

    mat_vals = np.zeros((2,2))
    res_vals = np.zeros((1,2))

    res = 0
    
    for machine in machines:
        for i in range(len(machine)):
            if i < 2:
                mat_vals[i] = re.findall('\+(\d+)', machine[i])
            else:
                res_vals[0] = re.findall('=(\d+)', machine[i])

        res_vals = res_vals + 10000000000000
        #solving xA = b
        solved = (res_vals) @ np.linalg.inv(mat_vals)

        #fixing the decimals
        solved = np.round(solved)

        if np.all(solved @ mat_vals == res_vals):
            res += np.sum(solved * (3, 1))

    print(res)




if __name__ == '__main__':
    main()
