def main():
    with open('day_9.in', 'r') as f:
        stream = f.read()

        score = 0
        garbage, cancelled = False, False

        for c in stream:
            if c == '!':
                cancelled = not cancelled
                continue

            if c == '<' and not cancelled:
                if garbage:
                    score += 1
                garbage = True
            elif c == '>' and not cancelled:
                garbage = False
            else:
                if garbage and not cancelled:
                    score += 1


            cancelled = False

        print(score)


if __name__ == '__main__':
    main()
