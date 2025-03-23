import argparse

def count_safe_reports(data): 
    count = 0

    for row in data.splitlines():
        report = [int(i) for i in row.split()]
        sign = ''
        for idx, num in enumerate(report):
            if idx != 0:
                dif = num - report[idx - 1]
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
                
            if idx == len(report) - 1:
                count += 1

    return count
            
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
            '-f', '--file',
            default = 'test.txt',
            help =  'The name of the file'
    )

    args = parser.parse_args()

    with open(args.file) as file:
        f = file.read()
    
    print(count_safe_reports(f))

if __name__ == '__main__':
    main()
