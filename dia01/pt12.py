import argparse
from collections import Counter

def data_parser(data):
    list1, list2 = [], [] 
    for row in data.splitlines():
        val1, val2 = row.split()
        list1.append(int(val1))
        list2.append(int(val2))

    return list1, list2

def total_dist(list1, list2):
    list1 = sorted(list1)
    list2 = sorted(list2)
    
    dist = sum([abs(x - y) for x, y in zip(list1, list2)])
    
    return dist
    

def similarity_score(list1, list2):
    res = 0
    count_list2 = Counter(list2)
    
    for val in list1:
        res += val * count_list2[val]
    
    return res
   
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-f', '--file', 
        default = 'test.txt',
        help = 'The name of the file'
    )
    
    args = parser.parse_args()

    with open(args.file) as file:
        f = file.read()
        parsed_data = data_parser(f)
    
    print(total_dist(*parsed_data))
    print(similarity_score(*parsed_data))

if __name__ == '__main__':
    main()
