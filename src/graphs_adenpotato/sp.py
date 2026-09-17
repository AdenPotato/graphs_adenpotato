import sys
from .heapq import heappush, heappop

def dijkstra(graph, source):
    """Compute the shortest paths from source to every vertex in graph.

    graph is an adjacency dict of the form {u: {v: weight, ...}, ...}.
    Returns (dist, path): dist maps each vertex to its lowest cost from
    source (sys.maxsize if unreachable), and path maps each reachable
    vertex to the list of vertices visited before reaching it.
    """
    # vertices that only appear as destinations still need a distance
    dist = {node: sys.maxsize for node in graph}
    for u in graph:
        for v in graph[u]:
            dist.setdefault(v, sys.maxsize)
    dist[source] = 0
    heap = []
    heappush(heap, (0, source))
    path = {source: []}

    while heap:
        w, u = heappop(heap)
        if w > dist[u]:
            # stale entry: a cheaper route to u was already processed
            continue
        for v in graph.get(u, {}):
            if w + graph[u][v] < dist[v]:
                dist[v] = w + graph[u][v]
                heappush(heap, (dist[v], v))
                path[v] = path[u] + [u]

    return dist, path
