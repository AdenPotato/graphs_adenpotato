from collections import deque

def bfs(graph, source):
    """Return the vertices reachable from source in breadth-first order.

    graph is an adjacency dict of the form {u: {v: weight, ...}, ...}.
    """
    visited = {source}
    order = []
    queue = deque([source])

    while queue:
        u = queue.popleft()
        order.append(u)
        for v in graph.get(u, {}):
            if v not in visited:
                visited.add(v)
                queue.append(v)

    return order

def dfs(graph, source):
    """Return the vertices reachable from source in depth-first order.

    graph is an adjacency dict of the form {u: {v: weight, ...}, ...}.
    """
    visited = set()
    order = []
    stack = [source]

    while stack:
        u = stack.pop()
        if u in visited:
            continue
        visited.add(u)
        order.append(u)
        # push neighbors in reverse so they are visited in insertion order
        for v in reversed(list(graph.get(u, {}))):
            if v not in visited:
                stack.append(v)

    return order
