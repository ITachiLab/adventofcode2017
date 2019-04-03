from collections import defaultdict


def main():
    with open('day_8.in', 'r') as f:
        regs = defaultdict(int)
        highest = -99999

        for l in f.readlines():
            # 0  1   2   3  4  5  6
            # es inc 278 if ib > -9
            parts = l.strip().split(' ')
            condition = f'regs[\'{parts[4]}\'] {parts[5]} {parts[6]}'

            if eval(condition):
                if parts[1] == 'inc':
                    regs[parts[0]] += int(parts[2])
                else:
                    regs[parts[0]] -= int(parts[2])

                if regs[parts[0]] > highest:
                    highest = regs[parts[0]]

        print(highest)


if __name__ == '__main__':
    main()