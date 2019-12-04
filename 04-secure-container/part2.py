def digits(n):
    return list(map(int, str(n)))


def decreases(n):
    for a, b in zip(n, n[1:]):
        if b < a:
            return True
    return False


def double_not_tripple(n):
    n = [-1] + n + [-1]
    for a, b, c, d in zip(n, n[1:], n[2:], n[3:]):
        if b == c and a != b and c != d:
            return True
    return False


def gen(n1, n2):
    for n in range(n1, n2):
        d = digits(n)
        if decreases(d):
            continue
        if not double_not_tripple(d):
            continue
        yield n


def count(n1, n2):
    return len(list(gen(n1, n2)))


if __name__ == '__main__':
    n1, n2 = map(int, input().split('-'))
    print(count(n1, n2))
