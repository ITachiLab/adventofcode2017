def main():
    with open('day_5.in', 'r') as f:
        instructions = [int(l) for l in f.readlines()]
        steps, index = 0, 0

        while True:
            try:
                next = index + instructions[index]
                instructions[index] += 1
                index = next
                steps += 1
            except IndexError:
                break

        print(steps)
                
if __name__ == '__main__':
    main()
