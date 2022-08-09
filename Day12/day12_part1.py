# result is a using heavily https://stackoverflow.com/a/33470137

from collections import defaultdict


class CaveCounter:
    def __init__(self):
        self.counter = 0

    def get_counter(self):
        return self.counter

    def add_counter(self):
        self.counter += 1


def read_input():
    graph = defaultdict(list)

    for line in open('day12.dat'):
        a, b = line.strip().split('-')
        graph[a].append(b)
        graph[b].append(a)

    return graph


def dfs_path(graph, start, end, count):
    result = []
    dfs(graph, start, end, [], result, count)
    return result


def dfs(graph, start, end, path, result, count):
    path += [start]
    if start == end:
        result.append(path)
        count.add_counter()
    else:
        for node in graph[start]:
            if not node.islower() or node not in path:
                dfs(graph, node, end, path[:], result, count)


part1 = CaveCounter()
data = read_input()
dfs_path(data, 'start', 'end', part1)
print(part1.get_counter())
assert part1.get_counter() == 4792
