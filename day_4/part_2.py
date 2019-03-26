def is_anagram(first, second):
    return sorted(list(first)) == sorted(list(second))

def main():
    valid = 0

    with open('day_4.in', 'r') as f:
        for l in f.readlines():
            split = l.strip().split(' ')
            valid_passphrase = True

            for start in range(0, len(split) - 1):
                for cur in range(start + 1, len(split)):
                    if is_anagram(split[start], split[cur]):
                        valid_passphrase = False
                        break
                if not valid_passphrase:
                    break

            if valid_passphrase:
                valid += 1

    print(valid)

if __name__ == '__main__':
    main()