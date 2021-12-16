# Inspired by https://github.com/alexander-yu/adventofcode/blob/master/utils.py

import networkx as nx


def read_input(filename: str = "day15.dat") -> list:
    with open(filename, "r") as f:
        data = [list(d.rstrip()) for d in f.readlines()]
    data = [[int(item) for item in line] for line in data]
    return data


def shortest_route(risk: list) -> int:
    # nx.grid_2d_graph is a 2d grid graph of mxn nodes, each connected to its nearest neighbors
    # nx.DiGraph stores nodes and edges with optional data, or attributes.
    columns = len(risk[0])
    rows = len(risk)
    G = nx.grid_2d_graph(rows, columns, create_using=nx.DiGraph)

    # add risk (weight) to "step" between u and v.
    for u, v in G.edges():
        G.edges[u, v]['risk'] = risk[v[0]][v[1]]

    # assign start and stop
    start = (0, 0)
    end = (len(risk) - 1, len(risk[0]) - 1)

    # calculate dijkstra_path_length from start to end:
    route = nx.dijkstra_path_length(G, start, end, weight='risk')

    return route


def multiply_map(two_dim_list: list, multiplier: int = 5) -> list:
    # extend lines down
    upper = two_dim_list[:]
    next_down = []
    new_list = []
    new_list.extend(upper)

    for i in range(multiplier-1):
        for line in upper:
            to_be_add = list(map(lambda item: (1, item+1)[item+1 <= 9], line))
            next_down.append(to_be_add)
        new_list.extend(next_down)
        upper = next_down[:]
        next_down = []

    # extend each line left
    for line in new_list:
        next_line = line[:]
        for i in range(multiplier - 1):
            to_be_add = list(map(lambda item: (1, item + 1)[item + 1 <= 9], next_line))
            line.extend(to_be_add)
            next_line = to_be_add[:]

    return new_list


def print_map(two_dim_list):
    for line in two_dim_list:
        print(line)


chiton_data = read_input("day15.dat")

part1 = shortest_route(chiton_data)
print(part1)
assert part1 == 811

part2 = shortest_route(multiply_map(chiton_data))
print(part2)
assert part2 == 3012
