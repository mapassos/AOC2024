def main():

    with open('input.txt') as f:
        f_content = [line for line in f.read().splitlines()]

    ans = []
    eqs = []

    for line in f_content:
        line_splitted = line.split(': ')
        ans.append(int(line_splitted[0]))
        eqs.append(list(map(int, line_splitted[1].split())))


    ops = [
        lambda a, b: a + b,
        lambda a, b: a * b,
        lambda a, b: int(str(a) + str(b))
        ]

    correct_ans = set()

    for i, eq in enumerate(eqs):
        possible_ops(eq[0], ans[i], eq[1:], ops, correct_ans)

    print(sum(i for i in correct_ans))

def possible_ops(res, ans, vals, ops, correct_ans):
    if len(vals) > 0:
        for op in ops:
            old_val = res
            res = op(res, vals[0])
            possible_ops(res, ans, vals[1:], ops, correct_ans)
            res = old_val
    else:
        if res == ans:
            correct_ans.add(ans)
        return
    return 


        

if __name__ == '__main__':
    main()
