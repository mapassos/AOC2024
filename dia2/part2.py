def main():
    with open('input.txt') as file:
        f_cont = file.read()

    count = 0
    mat = [list(map(int, row.split())) for row in f_cont.splitlines()] 
    for arr in mat:
        if any(all([increasing(arr[:i] + arr[i+1:]) or decreasing(arr[:i] + arr[i+1:]), dif_safety(arr[:i] + arr[i+1:])]) for i in range(len(arr))):
            count += 1
    
    print(count)
    
def increasing(arr):
    dif = [arr[idx] - arr[idx - 1] for idx in range(1, len(arr)) if arr[idx] - arr[idx - 1] > 0]
    if len(dif) == len(arr) - 1:
        return True
    else:
        return False

def decreasing(arr):
    dif = [arr[idx] - arr[idx - 1] for idx in range(1, len(arr)) if arr[idx] - arr[idx - 1] < 0]
    if len(dif) == len(arr) - 1:
        return True
    else:
        return False

def dif_safety(arr):
    dif = [arr[idx] - arr[idx - 1] for idx in range(1, len(arr)) if abs(arr[idx] - arr[idx - 1]) <= 3]
    if len(dif) == len(arr) - 1:
        return True
    else:
        return False

if __name__ == '__main__':
    main()
