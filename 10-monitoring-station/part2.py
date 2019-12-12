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
    return sorted(count, key=lambda x: x[1], reverse=True)[0][0]


def angles_and_distances(roids, best_x, best_y):
    data = {}
    for x, y in roids:
        xd = best_x - x
        yd = best_y - y
        if xd == 0 and yd == 0:
            continue
        ang = math.atan2(xd, yd) * -1
        if ang not in data:
            data[ang] = []
        data[ang].append(((x, y), math.sqrt(xd**2 + yd**2)))

    return data


def zap_zap(data):
    last = None
    n = 200
    while len(data.keys()) > 1 and n > 0:
        n -= 1
        items = sorted(data.items(), key=lambda x: x[0])
        items = [
            item for item in items if item[0] >= 0
        ] + [item for item in items if item[0] < 0]
        data = {}
        for ang, roids in items:
            print(ang, roids)
            last = roids[0]
            if len(roids) > 1:
                data[ang] = sorted(roids, key=lambda x: x[1])[1:]

    return last[0]


if __name__ == '__main__':
    roids, x, y = read_map()
    count = count_angles(roids)
    best = bestest(count)
    data = angles_and_distances(roids, *best)
    last = zap_zap(data)
    print(last)
