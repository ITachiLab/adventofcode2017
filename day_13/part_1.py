class Firewall:
    def __init__(self, depth, width):
        self.depth = depth
        self.range = width
        self.scanner_position = 0
        self.scanner_direction = 1
        self.severity = depth * width

    def move_scanner(self):
        if self.scanner_position == self.range - 1:
            self.scanner_direction = -1
        elif self.scanner_position == 0:
            self.scanner_direction = 1

        self.scanner_position += self.scanner_direction

    def can_catch(self):
        return self.scanner_position == 0


def main():
    firewalls = {}

    with open('day_13.in', 'r') as f:
        for l in f.readlines():
            entry = l.strip().replace(' ', '').split(':')
            firewalls[entry[0]] = Firewall(int(entry[0]), int(entry[1]))

        last = int(entry[0])
        severity_sum = 0

        for p in range(0, last + 1):
            f = firewalls[str(p)] if str(p) in firewalls else None

            if f and f.can_catch():
                severity_sum += f.severity

            for firewall in firewalls.values():
                firewall.move_scanner()

        print(severity_sum)

if __name__ == '__main__':
    main()
