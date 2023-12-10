

def day9():
    print("=== Day 9: Mirage Maintenance ===")
    with open("input/day9.txt") as f:
        data = f.read().replace("\r\n", "\n")

    values = list(map(lambda line: list(map(int, line.split(" "))), data.split("\n")))
    print("-- Part 1: --")
    sum_of_next = sum(map(calculate_next, values))
    print("The sum of all the next values is ", sum_of_next)
    print()
    print("-- Part 2: --")
    sum_of_prev = sum(map(calculate_prev, values))
    print("The sum of all the previous values is ", sum_of_prev)


def calculate_next(values):
    layers = make_layers(values)
    for i in range(len(layers) - 1):
        index = len(layers) - 1 - i
        layers[index - 1].append(layers[index][-1] + layers[index - 1][-1])
    return layers[0][-1]


def calculate_prev(values):
    layers = make_layers(values)
    num = 0
    for layer in reversed(layers):
        num = layer[0] - num
    return num


def make_layers(values):
    layers = [values]
    while not is_all_zero(layers[-1]):
        layers.append(calculate_next_layer(layers[-1]))
    return layers


def calculate_next_layer(values):
    next_layer = []
    for i in range(len(values) - 1):
        next_layer.append(values[i + 1] - values[i])
    return next_layer


def is_all_zero(values):
    return all(i == 0 for i in values)
