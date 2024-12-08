from collections import Counter

def main():

    with open('test.txt') as file:
        f_cont = file.read()

    left_list, right_list = [], [] 
    for row in f_cont.splitlines():
        left_val, right_val = row.split()
        left_list.append(int(left_val))
        right_list.append(int(right_val))

    dist = sum([abs(x - y) for x, y in zip(sorted(left_list), sorted(right_list))])
    print(dist)
    
    similarity_score(left_list, right_list)
    input('---')


def similarity_score(list1, list2):
    res = 0

    count_list2 = Counter(list2)
    for val in list1:
        res += val * count_list2[val]
    print(res)
    
    
if __name__ == '__main__':
    main()
