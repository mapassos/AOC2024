import re

def main():
    with open('test.txt') as f:
        txt = f.read()

    res = 0
    split_donts = txt.split("don't()")
    res += sum([eval(op) for op in re.findall(r'mul\(\d+,\d+\)', split_donts[0])])
    
    for donts in split_donts[1:]:
        split_dos = donts.split('do()')
        for dos in split_dos[1:]:
            res += sum([eval(op) for op in re.findall(r'mul\(\d+,\d+\)', dos)])

    print(res)
    input('----')
    
def mul(x, y):
    return x * y

if __name__ ==  '__main__':
    main()
