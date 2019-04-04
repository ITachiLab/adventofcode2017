class CircleList(list):
    def __setitem__(self, key, value):
        list.__setitem__(self, key % self.__len__(), value)

    def __getitem__(self, item):
        return list.__getitem__(self, item % self.__len__())

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
        input = list(map(int, f.readline().strip().split(',')))

        for length in input:
            reverse(elements, index, length)

            index += skip + length
            skip += 1

    print(elements[0] * elements[1])


if __name__ == '__main__':
    main()