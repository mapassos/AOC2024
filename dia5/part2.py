from collections import defaultdict
import time

def main():
    with open('input.txt') as f:
        f_read = f.read().split('\n\n')

    rules = f_read[0]
    updates = f_read[1]
    rule_book = defaultdict(list)

    for rule in rules.splitlines():
        rule_split = rule.split('|')
        rule_book[rule_split[0]].append(rule_split[1])

    corrected = []
    for section in updates.splitlines():
        section = [num for num in section.split(',')]
        if not check_update(section, rule_book):
            corrected_section = correct_update(section, rule_book)
            while not check_update(corrected_section, rule_book):
                corrected_section = correct_update(corrected_section, rule_book)
            corrected.append(corrected_section)

    #all lengths are odd
    mid_vals = [int(cor[len(cor) // 2]) for cor in corrected]
    res = sum(mid_vals)

    print(res)
    input('---')

def check_update(section, rules):
    for rule in rules:
        if rule in section:
            pos = section.index(rule)
            for val in rules[rule]:
                if val in section and pos > section.index(val):
                    return False
    return True

def correct_update(section, rules):
    for rule in rules:
        if rule in section:
            rulepos = section.index(rule)
            for val in rules[rule]:
                if val in section:
                    valpos = section.index(val)
                    if rulepos > valpos:
                        section[rulepos], section[valpos] = section[valpos], section[rulepos]
    return section

if __name__ == '__main__':
    main()
