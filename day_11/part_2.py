def main():
    steps = {
        'n': 0.0,
        'e': 0.0,
        's': 0.0,
        'w': 0.0
    }

    opposite = {
        'n': 's',
        's': 'n',
        'w': 'e',
        'e': 'w'
    }

    with open('day_11.in', 'r') as f:
        path = f.read().strip().split(',')
        furthest = 0

        for step in path:
            if len(step) == 2:
                for s in step:
                    op = opposite[s]

                    if steps[op] > 0:
                        steps[op] -= 0.5
                    else:
                        steps[s] += 0.5
            else:
                op = opposite[step]

                if steps[op] >= 1:
                    steps[op] -= 1
                elif steps[op] == 0.5:
                    steps[op] -= 0.5
                    steps[step] += 0.5
                else:
                    steps[step] += 1

            distance = sum(steps.values())

            if distance > furthest:
                furthest = distance

        print(furthest)


if __name__ == '__main__':
    main()