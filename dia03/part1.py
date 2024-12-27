import re

def main():
    with open('test.txt') as f:
        txt = f.read()

    res = 0

    filt = re.findall(r'mul\(\d+,\d+\)', txt)
    for op in filt:
        res += eval(op)    
    print(res)
    input('---')
    
def mul(x, y):
    return x * y

if __name__ ==  '__main__':
    main()
