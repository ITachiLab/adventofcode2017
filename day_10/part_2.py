from functools import reduce

class CircleList(list):
    def __setitem__(self, key, value):
        list.__setitem__(self, key % self.__len__(), value)

    def __getitem__(self, item):
        return list.__getitem__(self, item % self.__len__())


def chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]


def reverse(array, start, count):
    if count <= 1:
        return

    first_pointer = start
    second_pointer = start + (count - 1)

    while first_pointer < second_pointer:
        array[first_pointer], array[second_pointer] = array[second_pointer], array[first_pointer]
        first_pointer += 1
        second_pointer -= 1


def main():
    elements = CircleList(range(0, 256))
    skip = 0
    index = 0

    with open('day_10.in', 'r') as f:
        input = list(map(ord, f.readline().strip())) + [17, 31, 73, 47, 23]

        for i in range(0, 64):
            for length in input:
                reverse(elements, index, length)

                index += skip + length
                skip += 1

    elements = list(elements)
    dense_hash = [hex(reduce(lambda n1, n2: n1 ^ n2, chunk)).split('0x')[1].zfill(2) for chunk in chunks(elements, 16)]


    print(''.join(dense_hash))


if __name__ == '__main__':
    main()