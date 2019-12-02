def computer(code):
    i = 0
    while True:
        o = code[i]
        if o == 99:
            break
        a = code[i + 1]
        b = code[i + 2]
        c = code[i + 3]
        if o == 1:
            code[c] = code[a] + code[b]
        elif o == 2:
            code[c] = code[a] * code[b]
        i = i + 4
    return code[0]


if __name__ == '__main__':
    data = input()
    code = list(map(int, data.split(',')))
    code[1] = 12
    code[2] = 2
    print(computer(code))
