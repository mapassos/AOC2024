import re

def main():
    with open('input.txt') as f:
        txt = f.read()

    res = 0
    for line in txt.splitlines():
        filt = re.findall(r'mul\(\d+,\d+\)', line)
        for op in filt:
            res += eval(op)    
    print(res)
    
def mul(x, y):
    return x * y

if __name__ ==  '__main__':
    main()
