def main():
    sum = 0

    with open('day_1.in', 'r') as f:
        content = list(f.read())
        step = len(content) / 2

        for index, n in enumerate(content):
            if n == content[int((index + step) % len(content))]:
                sum += int(n)

        print(sum)

if __name__ == '__main__':
    main()