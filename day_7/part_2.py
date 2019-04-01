import re


class Disk():
    def __init__(self, name):
        self.name = name
        self.parents = []
        self.subnodes = []
        self.weight = 0
        self.__total_weight = None

    @property
    def total_weight(self):
        if self.__total_weight is None:
            self.__total_weight = sum([sub.total_weight for sub in self.subnodes]) + self.weight

        return self.__total_weight

    @property
    def child_count(self):
        return len(self.subnodes)


suspicious = None


def search(node):
    global suspicious

    if node.child_count > 1:
        weight_pairs = [(sub, sub.total_weight) for sub in node.subnodes]
        weight_pairs.sort(key=lambda x: x[1])

        weights = [x[1] for x in weight_pairs]

        if len(set(weights)) != 1:
            first_node = weight_pairs[0]
            second_node = weight_pairs[-1]

            if weights.count(first_node[1]) > weights.count(second_node[1]):
                selected = second_node
                other = first_node
            else:
                selected = first_node
                other = second_node

            if selected[0].child_count > 0:
                suspicious = (selected[0], (other[0].total_weight - selected[0].total_weight) + selected[0].weight)
                search(suspicious[0])
            else:
                return
    else:
        return


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
        
        search(base)

        print(f'{suspicious[0].name} -> {suspicious[1]}')


if __name__ == '__main__':
    main()
