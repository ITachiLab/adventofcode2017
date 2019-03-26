def main():
    valid = 0

    with open('day_4.in', 'r') as f:
        for l in f.readlines():
            split = l.strip().split(' ')

            if len(split) == len(set(split)):
                print(split)
                valid += 1

    print(valid)

if __name__ == '__main__':
    main()