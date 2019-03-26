from sys import argv

def spiral():
    x, y = 0, 0
    value, increment, delta = 1, 1, 1

    while True:
        for i in range(0, increment):
            x += delta
            value += 1

            yield x, y, value

        for i in range(0, increment):
            y += delta
            value += 1

            yield x, y, value

        increment += 1
        delta = -delta

def main():
    input = int(argv[1])

    for x, y, value in spiral():
        if value == input:
            found_x = x
            found_y = y
            break

    print(abs(0 - found_x) + abs(0 - found_y))

if __name__ == '__main__':
    main()