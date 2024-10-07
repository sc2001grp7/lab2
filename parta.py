from typing import List

def dijkstra(graph: List[List[int]], source: int):
    d = [float('inf')] * len(graph)
    # an array of length |V| to store the estimated LENGTHS of shortest paths from source to all vertices

    pi = [None] * len(graph)
    # an array of length |V| to store the PREDECESSORS of each vertex

    s = [False] * len(graph)
    # an array of length |V| to store whether the shortest path to the vertex has been found

    d[source] = 0
    q = [d[i] for i in range(len(graph))]
    q_size = 1
    while q_size:
        u = q.index(min(q))
        q[u] = float('inf')
        q_size -= 1
        s[u] = True
        for v, weight in enumerate(graph[u]):
            if s[v] == False and d[v] > d[u] + weight:
                d[v] = d[u] + weight
                pi[v] = u
                q[v] = d[v]
                q_size += 1

    return d, pi
