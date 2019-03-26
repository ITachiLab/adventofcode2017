from re import split

def main():
    checksum = 0

    with open('day_2.in', 'r') as f:
        for l in f.readlines():
            row = [int(x) for x in split(' +', l)]
            checksum += max(row) - min(row)

    print checksum

if __name__ == '__main__':
    main()