class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)


def earliest_ancestor(ancestors, starting_node, visited=None):
    values = []
    keys = []

    for pair in ancestors:
        keys.append(pair[0])
        values.append(pair[1])
    if visited is None:
        visited = set()
    if starting_node not in values and starting_node not in visited:
        return -1
    for pair in ancestors:
        if pair[1] == starting_node:
            visited.add(pair[0])
            return earliest_ancestor(ancestors, pair[0], visited)
    return starting_node
