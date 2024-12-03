def main():
    with open('input.txt') as file:
        f_cont = file.read()

    count = 0
    
    for row in f_cont.splitlines():
        list = [int(i) for i in row.split()]
        sign = ''
        for idx, num in enumerate(list):
            if idx != 0:
                dif = num - list[idx - 1]
                if dif < 0 and sign == '+':
                    break
                
                elif dif < 0:
                    sign = '-'
                    
                elif dif > 0 and sign == '-':
                    break
                
                elif dif > 0:
                    sign = '+'
                    
                else:
                    break
                
                if abs(dif) > 3:
                    break
                
            if idx == len(list) - 1:
                count += 1
            
                
    print(count)

if __name__ == '__main__':
    main()
