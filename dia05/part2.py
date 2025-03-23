from collections import defaultdict
import argparse

def apply_rule(page):
    rules = page[0]
    updates = page[1]
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

    return res

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
