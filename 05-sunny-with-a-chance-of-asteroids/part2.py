from functools import partial


def op_and_modes(n):
    d = list(map(int, reversed(str(n))))
    if len(d) > 1:
        op = d[0] + (d[1] * 10)
    else:
        op = d[0]
    return op, d[2:]


def _read(code, modes, i, o):
    try:
        mode = modes[o - 1]
    except IndexError:
        mode = 0
    if mode == 1:
        return code[i + o]
    else:
        return code[code[i + o]]


def _write(code, modes, i, o, v):
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
        op, modes = op_and_modes(code[i])
        write = partial(_write, code, modes, i)
        read = partial(_read, code, modes, i)
        if op == 99:
            break
        elif op == 1:
            v = read(1) + read(2)
            write(3, v)
            i += 4
        elif op == 2:
            v = read(1) * read(2)
            write(3, v)
            i += 4
        elif op == 3:
            v = int(input())
            write(1, v)
            i += 2
        elif op == 4:
            print(read(1))
            i += 2
        elif op == 5:
            if read(1) != 0:
                i = read(2)
            else:
                i += 3
        elif op == 6:
            if read(1) == 0:
                i = read(2)
            else:
                i += 3
        elif op == 7:
            write(3, int(read(1) < read(2)))
            i += 4
        elif op == 8:
            write(3, int(read(1) == read(2)))
            i += 4
        else:
            raise Exception(f'fuck, op: {op}, modes: {modes}')

    return code[0]


if __name__ == '__main__':
    code = list(map(int, input().split(',')))
    advanced_computer(code)
