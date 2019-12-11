class Computer:

    def __init__(self, prog, i=0, b=0, inp=None, out=None):

        self.prog = prog
        self.i = i
        self.b = b
        if inp is None:
            inp = []
        if out is None:
            out = []
        self.inp = inp
        self.out = out
        self.op = None
        self.modes = None

    def set_op_and_modes(self):
        n = self.prog[self.i]
        d = list(map(int, reversed(str(n))))
        if len(d) > 1:
            op = d[0] + (d[1] * 10)
        else:
            op = d[0]
        self.op = op
        self.modes = d[2:]

    def extend(self, n):
        if n > len(self.prog):
            self.prog += [0] * (n - len(self.prog))

    def read(self, o, mode=None):
        if mode is None:
            try:
                mode = self.modes[o - 1]
            except IndexError:
                mode = 0
        if mode == 1:
            addr = self.i + o
        elif mode == 2:
            addr = self.b + o
        else:
            return self.prog[self.prog[self.i + o]]
        
        return self.prog[addr]


    def write(self, o, v):
        try:
            mode = self.modes[o - 1]
        except IndexError:
            mode = 0
        if mode == 1:
            self.prog[self.i + o] = v
        elif mode == 2:
            self.prog[self.b + o] = v
        else:
            self.prog[self.prog[self.i + o]] = v


    def run(self):
        blocked = False
        while True:
            self.set_op_and_modes()
            if self.op == 99:
                break
            elif self.op == 1:
                v = self.read(1) + self.read(2)
                self.write(3, v)
                self.i += 4
            elif self.op == 2:
                v = self.read(1) * self.read(2)
                self.write(3, v)
                self.i += 4
            elif self.op == 3:
                try:
                    v = self.inp.pop()
                except IndexError:
                    blocked = True
                    break
                self.write(1, v)
                self.i += 2
            elif self.op == 4:
                self.out.append(self.read(1))
                self.i += 2
            elif self.op == 5:
                if self.read(1) != 0:
                    self.i = self.read(2)
                else:
                    self.i += 3
            elif self.op == 6:
                if self.read(1) == 0:
                    self.i = self.read(2)
                else:
                    self.i += 3
            elif self.op == 7:
                self.write(3, int(self.read(1) < self.read(2)))
                self.i += 4
            elif self.op == 8:
                self.write(3, int(self.read(1) == self.read(2)))
                self.i += 4
            elif self.op == 9:
                self.b += self.read(1)
                self.i += 2
            else:
                raise Exception(f'fuck, op: {self.op}, modes: {self.modes}')

        return self.prog[0], blocked, self.i
