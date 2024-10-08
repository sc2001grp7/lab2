import random
import timeit

import tqdm
import numpy as np

from parta import dijkstra as dijkstra_matrix_array
from partb import Dijkstra_ShortestPath as dijkstra_list_heap

def generate_weighted_undirected_graph(n: int, m: int):
    assert n > 0 and m > 0 and m <= n*(n-1)//2

    edges = np.array(np.triu_indices(n, 1)).T
    g_matrix = np.full((n, n), float('inf')).tolist()
    g_list = {}

    print("Generating random graph...")
    selected_edges = edges[np.random.choice(edges.shape[0], m, replace=False)].tolist()
    weights = np.random.randint(1, 101, size=m).tolist()

    for (u, v), w in tqdm.tqdm(zip(selected_edges, weights), total=m):
        g_matrix[u][v] = w
        g_matrix[v][u] = w
        if u not in g_list:
            g_list[u] = {}
        g_list[u][v] = w
        if v not in g_list:
            g_list[v] = {}
        g_list[v][u] = w

    return g_matrix, g_list

if __name__ == "__main__":
    # random.seed(42)
    n = 1000
    runs = 10

    # Generate a random sparse graph (m = n - 1)
    m = n - 1
    g_matrix, g_list = generate_weighted_undirected_graph(n, m)
    timeit_a = timeit.timeit(lambda: dijkstra_matrix_array(g_matrix, 0), number=runs)
    timeit_b = timeit.timeit(lambda: dijkstra_list_heap(g_list, 0), number=runs)
    print(f"Avg time for adjacency matrix and array pq implementation (n={n}, m={m}, runs={runs}):")
    print(timeit_a, "seconds")
    print(f"Avg time for adjacency list and min heap pq implementation (n={n}, m={m}, runs={runs}):")
    print(timeit_b, "seconds")
    print()

    # Generate a random dense graph (m = n(n-1)/2)
    m = n*(n-1)//2
    g_matrix, g_list = generate_weighted_undirected_graph(n, m)
    timeit_a = timeit.timeit(lambda: dijkstra_matrix_array(g_matrix, 0), number=runs)
    timeit_b = timeit.timeit(lambda: dijkstra_list_heap(g_list, 0), number=runs)
    print(f"Avg time for adjacency matrix and array pq implementation (n={n}, m={m}, runs={runs}):")
    print(timeit_a, "seconds")
    print(f"Avg time for adjacency list and min heap pq implementation (n={n}, m={m}, runs={runs}):")
    print(timeit_b, "seconds")
    print()

    # Generate a random graph (2n <= m <= n(n-1)/2)
    m = random.randint(2*n, n*(n-1)//2)
    g_matrix, g_list = generate_weighted_undirected_graph(n, m)
    timeit_a = timeit.timeit(lambda: dijkstra_matrix_array(g_matrix, 0), number=runs)
    timeit_b = timeit.timeit(lambda: dijkstra_list_heap(g_list, 0), number=runs)
    print(f"Avg time for adjacency matrix and array pq implementation (n={n}, m={m}, runs={runs}):")
    print(timeit_a, "seconds")
    print(f"Avg time for adjacency list and min heap pq implementation (n={n}, m={m}, runs={runs}):")
    print(timeit_b, "seconds")
    print()
