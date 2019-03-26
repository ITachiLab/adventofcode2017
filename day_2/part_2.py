from re import split

def finder(row):
    for i1, n1 in enumerate(row):
        for i2, n2 in enumerate(row):
            if i1 == i2:
                continue

            if (n1 % n2) == 0:
                return n1 / n2

def main():
    checksum = 0

    with open('day_2.in', 'r') as f:
        for l in f.readlines():
            row = [int(x) for x in split(' +', l)]
            checksum += finder(row)

    print checksum

if __name__ == '__main__':
    main()