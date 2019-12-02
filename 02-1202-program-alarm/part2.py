from part1 import computer

def reverse_computer(original, target):
    for noun in range(0, 100):
        for verb in range(100, 0, -1):
            code = [i for i in original]
            code[1] = noun
            code[2] = verb
            out = computer(code)
            if out < target:
                break
            if out == target:
                return noun, verb
    raise Exception('unable to reverse code to target')

if __name__ == '__main__':
    data = raw_input()
    original = map(int, data.split(','))
    noun, verb = reverse_computer(original, 19690720)
    print(100 * noun + verb)
