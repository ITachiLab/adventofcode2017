import re

class Disk():
    def __init__(self, name):
        self.name = name
        self.parents = []
        self.subnodes = []
        self.weight = 0

def main():
    pattern = '^(?P<name>\\w+)\\s\\((?P<weight>\\d+)\\)$|^(?P<name2>\\w+)\\s\\((?P<weight2>\\d+)\\)\\s->\\s(?P<sub>.*)$'
    entries = {}

    with open('day_7.in', 'r') as f:
        for l in f.readlines():
            match = re.match(pattern, l)
            groups = match.groupdict()

            name = groups['name'] or groups['name2']
            weight = groups['weight'] or groups['weight2']
            sub = groups['sub'].replace(' ', '').split(',') if groups['sub'] is not None else []

            disk = Disk(name) if name not in entries else entries[name]

            disk.weight = int(weight)
            entries[name] = disk

            for node in sub:
                if node in entries:
                    disk.subnodes.append(entries[node])
                    entries[node].parents.append(disk)
                else:
                    new_disk = Disk(node)

                    entries[node] = new_disk
                    disk.subnodes.append(new_disk)
                    new_disk.parents.append(disk)

        base = next(d for d in entries.values() if len(d.parents) == 0)
        print(base.name)


if __name__ == '__main__':
    main()