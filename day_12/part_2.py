class Node:
    def __init__(self, id):
        self.id = id
        self.visited = False
        self.children = []

    def visit(self):
        self.visited = True

    def add_child(self, child):
        self.children.append(child)


def bfs(root):
    result = 0
    queue = [root]

    while len(queue):
        node = queue.pop(0)

        for c in node.children:
            if not c.visited:
                c.visit()
                result += 1
                queue.append(c)

    return result


def main():
    nodes = {}

    with open('day_12.in', 'r') as f:
        for l in f.readlines():
            entry = l.replace(' ', '').strip().split('<->')

            if entry[0] in nodes:
                node = nodes[entry[0]]
            else:
                node = Node(entry[0])
                nodes[entry[0]] = node

            children = entry[1].split(',')

            for c in children:
                if c in nodes:
                    child = nodes[c]
                else:
                    child = Node(c)
                    nodes[c] = child

                node.add_child(child)

        groups = 0

        for n in nodes.values():
            if not n.visited:
                bfs(n)
                groups += 1

        print(groups)

if __name__ == '__main__':
    main()
