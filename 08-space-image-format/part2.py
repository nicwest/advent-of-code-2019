def build_layers(data, x, y):
    layers = []
    n = x * y
    while data:
        layers.append(data[:n])
        data = data[n:]
    return layers


def build_image(layers, x, y):
    img = layers[-1]
    for layer in reversed(layers[:-1]):
        for i, p in enumerate(layer):
            if p < 2:
                img[i] = p
    return img


def display_image(img, x, y):
    for i in range(y):
        row = img[i * x: (i + 1) * x]
        print(*map(lambda x: '█' if x == 1 else ' ', row))


if __name__ == '__main__':
    data = list(map(int, input()))
    x = int(input())
    y = int(input())
    layers = build_layers(data, x, y)
    img = build_image(layers, x, y)
    display_image(img, x, y)
