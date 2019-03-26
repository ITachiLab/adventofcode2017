from sys import argv
from collections import defaultdict

def spiral():
    storage = defaultdict(lambda: defaultdict(int))
    x, y = 0, 0
    value, increment, delta = 1, 1, 1

    storage['0']['0'] = 1

    while True:
        for i in range(0, increment):
            x += delta
            storage[str(x)][str(y)] = \
                storage[str(x - 1)][str(y)] + \
                storage[str(x - 1)][str(y + 1)] + \
                storage[str(x)][str(y + 1)] + \
                storage[str(x + 1)][str(y + 1)] + \
                storage[str(x + 1)][str(y)] + \
                storage[str(x + 1)][str(y - 1)] + \
                storage[str(x)][str(y - 1)] + \
                storage[str(x - 1)][str(y - 1)]
            
            yield x, y, storage[str(x)][str(y)]

        for i in range(0, increment):
            y += delta
            storage[str(x)][str(y)] = \
                storage[str(x - 1)][str(y)] + \
                storage[str(x - 1)][str(y + 1)] + \
                storage[str(x)][str(y + 1)] + \
                storage[str(x + 1)][str(y + 1)] + \
                storage[str(x + 1)][str(y)] + \
                storage[str(x + 1)][str(y - 1)] + \
                storage[str(x)][str(y - 1)] + \
                storage[str(x - 1)][str(y - 1)]

            yield x, y, storage[str(x)][str(y)]

        increment += 1
        delta = -delta

def main():
    input = int(argv[1])

    for x, y, value in spiral():
        if value > input:
            print(value)
            break

if __name__ == '__main__':
    main()