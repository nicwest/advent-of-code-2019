def plot(wire):
    grid = {}
    x = y = 0
    s = 0
    for move in wire:
        direction = move[0]
        n = int(move[1:])
        for i in range(n):
            s += 1
            if direction == 'U':
                y += 1
            elif direction == 'R':
                x += 1
            elif direction == 'D':
                y -= 1
            elif direction == 'L':
                x -= 1
            if (x, y) not in grid:
                grid[(x, y)] = s
    return grid


def gen(wire_1, wire_2):
    grid_1 = plot(wire_1)
    grid_2 = plot(wire_2)

    for (x, y) in grid_1:
        if (x, y) in grid_2:
            yield grid_1[(x, y)] + grid_2[(x, y)]


def shortest_intersection(wire_1, wire_2):
    return min(gen(wire_1, wire_2))


if __name__ == '__main__':
    wire_1 = input().split(',')
    wire_2 = input().split(',')
    print(shortest_intersection(wire_1, wire_2))
