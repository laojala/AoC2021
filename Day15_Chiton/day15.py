# Inspired by https://github.com/alexander-yu/adventofcode/blob/master/utils.py

import networkx as nx

# read input data to 2D array of ints
with open("day15_example.dat", "r") as f:
    risk = [list(d.rstrip()) for d in f.readlines()]
risk = [[int(item) for item in line] for line in risk]

# nx.grid_2d_graph is a 2d grid graph of mxn nodes, each connected to its nearest neighbors
# nx.DiGraph stores nodes and edges with optional data, or attributes.
columns = len(risk[0])
rows = len(risk)
G = nx.grid_2d_graph(len(risk), len(risk[0]), create_using=nx.DiGraph)

# add risk (weight) to "step" between u and v.
for u, v in G.edges():
    G.edges[u, v]['risk'] = risk[v[0]][v[1]]

# assign start and stop
start = (0, 0)
end = (len(risk) - 1, len(risk[0]) - 1)

# calculate dijkstra_path_length from start to end:
part1 = nx.dijkstra_path_length(G, start, end, weight='risk')
print(part1)
assert part1 == 811


#
# start = (0, 0)
# end = (len(risk) - 1, len(risk[0]) - 1)
#
# G = nx.grid_2d_graph(len(risk), len(risk[0]))
#
# for u, v in G.edges():
#     print(risk[u[0]])
#     G.edges[u, v]['risk'] = risk[u[0]]
#
# print(G.edges)
#
# # def get_lowest_risk_path(grid):
# #     start = (0, 0)
# #     end = (grid.rows - 1, grid.columns - 1)
# #
# #     for u, v in grid.graph.edges():
# #         grid.graph.edges[u, v]['risk'] = grid[v]
# #
# #     return nx.dijkstra_path_length(grid.graph, start, end, weight='risk')
# #
