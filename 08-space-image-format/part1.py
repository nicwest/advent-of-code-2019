def build_layers(data, x, y):
    layers = []
    n = x * y
    while data:
        layers.append(data[:n])
        data = data[n:]
    return layers


def layer_with_least_zeros(layers):
    return sorted(
        [
            (i, sum([1 for d in layer if not d]))
            for i, layer in enumerate(layers)
        ],
        key=lambda x: x[1]
    )[0]


def ones_by_twos(layer):
    return sum(1 for i in layer if i == 1) * sum(1 for i in layer if i == 2)


if __name__ == '__main__':
    data = list(map(int, input()))
    layers = build_layers(data, int(input()), int(input()))
    zeroiest = layer_with_least_zeros(layers)
    print(ones_by_twos(layers[zeroiest[0]]))
