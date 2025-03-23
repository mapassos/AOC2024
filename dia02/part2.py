import argparse

def count_safe_reports(data):
    count = 0

    mat = [list(map(int, row.split())) for row in data.splitlines()] 
    for arr in mat:
        if any(
            all(
                [increasing(arr[:i] + arr[i+1:]) or decreasing(arr[:i] + arr[i+1:]), \
                        dif_safety(arr[:i] + arr[i+1:])]
            ) for i in range(len(arr))
        ):
            count += 1
   
    return count
    
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

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-f', '--file',
        default = 'test.txt',
        help = 'Name of the file'
    )
    
    args = parser.parse_args() 

    with open(args.file) as file:
        f = file.read()
    
    print(count_safe_reports(f))

if __name__ == '__main__':
    main()
