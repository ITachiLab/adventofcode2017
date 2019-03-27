def main():
    with open('day_5.in', 'r') as f:
        instructions = [int(l) for l in f.readlines()]
        steps, index = 0, 0

        while True:
            if index >= len(instructions):
                break

            next = index + instructions[index]

            if instructions[index] >= 3:
                instructions[index] -= 1
            else:
                instructions[index] += 1

            index = next
            steps += 1

        print(steps)
                
if __name__ == '__main__':
    main()
