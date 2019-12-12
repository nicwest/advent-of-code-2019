import math
import fileinput


def count_angles(roids):
    count = []
    for xa, ya in roids:
        count.append(
            (
                (xa, ya),
                len({
                    math.atan2(ya - yb, xa - xb)
                    for xb, yb in roids
                    if xa != xb or ya != yb
                }),
            )
        )
    return count


def read_map():
    roids = []
    for y, line in enumerate(fileinput.input()):
        for x, v in enumerate(line):
            if v == '#':
                roids.append((x, y))
    return roids, x, y


def bestest(count):
    return sorted(count, key=lambda x: x[1], reverse=True)[0]


if __name__ == '__main__':
    roids, x, y = read_map()
    count = count_angles(roids)
    print(bestest(count))
