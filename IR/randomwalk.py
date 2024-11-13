import numpy as np
import networkx as nx
import random

# Step 1: Create a directed graph with N nodes
G = nx.DiGraph()
edges = [
    (0, 1), (0, 2), (1, 3), (2, 3), (3, 0), (3, 1),
    (3, 4), (4, 5), (5, 6), (6, 4), (5, 7), (7, 5),
    (6, 8), (7, 8), (8, 5), (8, 6)
]
G.add_edges_from(edges)

# Step 2: Initialize parameters
N = len(G.nodes)
damping_factor = 0.85
iterations = 100000
initial_node = random.choice(list(G.nodes))
points = np.zeros(N)

# Step 3: Random Walk method
current_node = initial_node
for _ in range(iterations):
    points[current_node] += 1
    neighbors = list(G.successors(current_node))
    if neighbors:
        current_node = random.choice(neighbors)
    else:
        # Dead end: randomly jump to any node
        current_node = random.choice(list(G.nodes))

# Step 4: Normalize points to get probabilities
points = points / points.sum()
sorted_nodes_random_walk = np.argsort(points)[::-1]  # Sorted by importance

print("PageRank using Random Walk Method")
print(sorted_nodes_random_walk)

# Step 5: Compare with the inbuilt PageRank method
pagerank_builtin = nx.pagerank(G, alpha=damping_factor)
sorted_nodes_builtin = sorted(pagerank_builtin, key=pagerank_builtin.get, reverse=True)

print("\nPageRank using inbuilt pagerank method")
print(sorted_nodes_builtin)
