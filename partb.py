import heapq
from typing import Dict
def Dijkstra_ShortestPath(graph: Dict[int, Dict[int, int]], source: int):
  d = [float('infinity')] * len(graph)
  pi = [None] * len(graph)
  S = [0] * len(graph)
  Q = []
  vertices = set(graph.keys())
  for vertex in graph:
    vertices.update(graph[vertex].keys())
  for vertex in vertices:
    heapq.heappush(Q, (d[vertex], vertex))

  d[source] = 0
  for index, (dist, vertex) in enumerate(Q):
    if vertex == source:
      Q[index] = (0, source)
      break
  heapq.heapify(Q)

  while Q:
    _, u = heapq.heappop(Q)
    S[u] = 1
    for v, weight in graph.get(u, {}).items():
      if S[v] != 1 and d[v] > d[u] + weight:
        d[v] = d[u] + weight
        pi[v] = u
        heapq.heappush(Q, (d[v], v))
  return d, pi
