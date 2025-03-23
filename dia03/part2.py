import re
import argparse

def get_res(data):

    res = 0
    split_donts = data.split("don't()")
    res += sum([eval(op) for op in re.findall(r'mul\(\d+,\d+\)', split_donts[0])])
    
    for donts in split_donts[1:]:
        split_dos = donts.split('do()')
        for dos in split_dos[1:]:
            res += sum([eval(op) for op in re.findall(r'mul\(\d+,\d+\)', dos)])

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
