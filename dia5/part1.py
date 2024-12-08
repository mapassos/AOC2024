from collections import defaultdict

def main():
    with open('test.txt') as f:
        f_read = f.read().split('\n\n')

    rules = f_read[0]
    updates = f_read[1]
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
    print(res)
    input('---')

def check_update(section, rules):
    for rule in rules:
        pos = section.find(rule)
        for val in rules[rule]:
            if pos > section.find(val) >= 0:
                return False
    return True

if __name__ == '__main__':
    main()
