from computer import advanced_computer


class Amplifier:

    def __init__(self, setting, code, inp=None, out=None, i=0):
        self.code = code
        self.inp = inp
        self.out = out
        self.i = i
        self.exit = None
        self.completed = False
        self.setting = setting

    def run(self):
        if self.setting is not None:
            self.inp.append(self.setting)
            self.setting = None
        self.exit, blocked, self.i = advanced_computer(
            self.code, self.inp, self.out, self.i)
        if not blocked:
            self.completed = True


def gen_numbers(n, m):
    for a in range(n, m):
        for b in range(n, m):
            if a == b:
                continue
            for c in range(n, m):
                if c == b or c == a:
                    continue
                for d in range(n, m):
                    if d == c or d == b or d == a:
                        continue
                    for e in range(n, m):
                        if e == d or e == c or e == b or e == a:
                            continue
                        yield (a, b, c, d, e)


def amplify(code):
    out = []
    for a, b, c, d, e in gen_numbers(5, 10):
        amp_a = Amplifier(a, [i for i in code], inp=[0], out=[])
        amp_b = Amplifier(b, [i for i in code], inp=amp_a.out, out=[])
        amp_c = Amplifier(c, [i for i in code], inp=amp_b.out, out=[])
        amp_d = Amplifier(d, [i for i in code], inp=amp_c.out, out=[])
        amp_e = Amplifier(e, [i for i in code], inp=amp_d.out, out=amp_a.inp)

        while not amp_e.completed:
            amp_a.run()
            amp_b.run()
            amp_c.run()
            amp_d.run()
            amp_e.run()
        out.append((''.join(map(str, [a, b, c, d, e])), amp_e.out[0]))

    return sorted(out, key=lambda x: x[1], reverse=True)[0]


if __name__ == '__main__':
    code = list(map(int, input().split(',')))
    print(amplify(code))
