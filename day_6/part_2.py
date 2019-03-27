from re import split

def redist(mem):
    maxval = -1
    max_idx = 0

    for i, bank in enumerate(mem):
        if bank > maxval:
            max_idx = i
            maxval = bank

    idx = max_idx

    while mem[max_idx] != 0:
        idx = (idx + 1) % len(mem)

        if (idx == max_idx) and mem[max_idx] == 1:
            break

        mem[idx] += 1
        mem[max_idx] -= 1

    return mem

def main():
    results = []

    with open('day_6.in', 'r') as f:
        input = split('\\s+', f.readline().strip())
        memory = [int(x) for x in input]

        while memory not in results:
            results.append(memory)
            memory = redist(memory.copy())

        results = []

        while memory not in results:
            results.append(memory)
            memory = redist(memory.copy())

        print(len(results))

if __name__ == '__main__':
    main()
