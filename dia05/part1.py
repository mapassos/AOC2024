from collections import defaultdict
import argparse

def apply_rule(page):

    rules = page[0]
    updates = page[1]
    rule_book = defaultdict(list)

    for rule in rules.splitlines():
        rule_split = rule.split('|')
        rule_book[rule_split[0]].append(rule_split[1])

    corrects = []
    for update in updates.splitlines():
        if check_update(update, rule_book):
            corrects.append(update)


    corrects = [[int(num) for num in cor.split(',')] for cor in corrects]
    #all lengths are odd
    mid_vals = [cor[len(cor) // 2] for cor in corrects]
    res = sum(mid_vals)

    return res

def check_update(section, rules):
    for rule in rules:
        pos = section.find(rule)
        for val in rules[rule]:
            if pos > section.find(val) >= 0:
                return False
    return True

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-f', '--file',
        default = 'test.txt',
        help = 'Name of the file'
    )

    args = parser.parse_args()

    with open(args.file) as f:
        data = f.read().split('\n\n')
    
    print(apply_rule(data))

if __name__ == '__main__':
    main()
