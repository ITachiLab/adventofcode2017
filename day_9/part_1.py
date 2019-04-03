def main():
    with open('day_9.in', 'r') as f:
        stream = f.read()

        group, score = 0, 0
        garbage, cancelled = False, False

        for c in stream:
            if c == '!':
                cancelled = not cancelled
                continue

            if c == '{' and not garbage:
                group += 1
            elif c == '}' and not garbage:
                score += group
                group -= 1
            elif c == '<' and not garbage:
                garbage = True
            elif c == '>' and not cancelled:
                garbage = False

            cancelled = False

        print(score)


if __name__ == '__main__':
    main()
