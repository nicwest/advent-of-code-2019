def op_and_modes(n):
    d = list(map(int, reversed(str(n))))
    if len(d) > 1:
        op = d[0] + (d[1] * 10)
    else:
        op = d[0]
    return op, d[2:]


def read(code, modes, i, o):
    try:
        mode = modes[o - 1]
    except IndexError:
        mode = 0
    if mode == 1:
        return code[i + o]
    else:
        return code[code[i + o]]


def write(code, modes, i, o, v):
    try:
        mode = modes[o - 1]
    except IndexError:
        mode = 0
    if mode == 1:
        code[i + o] = v
    else:
        code[code[i+o]] = v


def advanced_computer(code):
    i = 0
    while True:
        # print(code)
        op, modes = op_and_modes(code[i])
        # print(op, modes)
        if op == 99:
            break
        elif op == 1:
            v = read(code, modes, i, 1) + read(code, modes, i, 2)
            write(code, modes, i, 3, v)
            i = i + 4
        elif op == 2:
            v = read(code, modes, i, 1) * read(code, modes, i, 2)
            write(code, modes, i, 3, v)
            i = i + 4
        elif op == 3:
            v = int(input())
            write(code, modes, i, 1, v)
            i = i + 2
        elif op == 4:
            print(read(code, modes, i,  1))
            i = i + 2
        else:
            raise Exception('fuck')

    return code[0]


if __name__ == '__main__':
    code = list(map(int, input().split(',')))
    advanced_computer(code)
