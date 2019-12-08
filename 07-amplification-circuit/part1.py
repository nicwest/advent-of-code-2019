from computer import advanced_computer


def gen_numbers():
    for a in range(5):
        for b in range(5):
            if a == b:
                continue
            for c in range(5):
                if c == b or c == a:
                    continue
                for d in range(5):
                    if d == c or d == b or d == a:
                        continue
                    for e in range(5):
                        if e == d or e == c or e == b or e == a:
                            continue
                        yield (a, b, c, d, e)


def amplify(code):
    out = []
    for a, b, c, d, e in gen_numbers():
        stack = [0, a]
        advanced_computer([i for i in code], stack)
        stack.append(b)
        advanced_computer([i for i in code], stack)
        stack.append(c)
        advanced_computer([i for i in code], stack)
        stack.append(d)
        advanced_computer([i for i in code], stack)
        stack.append(e)
        advanced_computer([i for i in code], stack)
        out.append((''.join(map(str, [a, b, c, d, e])), stack[0]))

    return sorted(out, key=lambda x: x[1], reverse=True)[0]


if __name__ == '__main__':
    code = list(map(int, input().split(',')))
    print(amplify(code))
