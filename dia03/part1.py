import re
import argparse

def get_res(data):
    res = 0

    filt = re.findall(r'mul\(\d+,\d+\)', data)
    for op in filt:
        res += eval(op)    
    
    return res
    
def mul(x, y):
    return x * y

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-f', '--file',
        default = 'test.txt',
        help = 'Name of the file'
    )

    args = parser.parse_args()

    with open(args.file) as f:
        data = f.read()

    print(get_res(data))

if __name__ ==  '__main__':
    main()
