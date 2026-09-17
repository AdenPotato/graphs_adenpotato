# graphs_adenpotato

A small, dependency-free Python library of graph algorithms. It currently provides:

| Module | Function | Description |
| --- | --- | --- |
| `sp` | `dijkstra(graph, source)` | Dijkstra's single-source shortest path algorithm (min-heap based) |
| `traversal` | `bfs(graph, source)` | Breadth-first traversal order from `source` |
| `traversal` | `dfs(graph, source)` | Depth-first traversal order from `source` |

## Links

- GitHub repository: https://github.com/AdenPotato/graphs_adenpotato
- PyPI package: https://pypi.org/project/graphs-adenpotato/

## Installation

Install from PyPI (Python 3.8+):

```
pip install graphs_adenpotato
```

Or install the latest code from GitHub:

```
pip install git+https://github.com/AdenPotato/graphs_adenpotato.git
```

Or clone and install locally:

```
git clone https://github.com/AdenPotato/graphs_adenpotato.git
cd graphs_adenpotato
pip install .
```

## Graph format

Graphs are plain dictionaries mapping each vertex to its neighbors and the weight of each edge:

```python
graph = {
    0: {1: 4, 7: 8},
    1: {0: 4, 2: 8, 7: 11},
    ...
}
```

Vertices may be any hashable value. Vertices that only appear as a destination (no outgoing edges) are handled too.

## Usage

### Shortest paths

```python
from graphs_adenpotato import sp

graph = {0: {1: 4, 2: 1}, 1: {3: 1}, 2: {1: 2, 3: 5}, 3: {}}
dist, path = sp.dijkstra(graph, 0)

print(dist)  # {0: 0, 1: 3, 2: 1, 3: 4}
print(path)  # {0: [], 1: [0, 2], 2: [0], 3: [0, 2, 1]}
```

- `dist[v]` is the lowest total weight to reach `v` from the source (`sys.maxsize` if `v` is unreachable).
- `path[v]` lists the vertices visited *before* `v` on a shortest path. Unreachable vertices are not in `path`.

Edge weights must be non-negative, as required by Dijkstra's algorithm.

### Traversals

```python
from graphs_adenpotato import traversal

traversal.bfs(graph, 0)  # [0, 1, 2, 3]
traversal.dfs(graph, 0)  # [0, 1, 3, 2]
```

## Running the example script

`test.py` reads a graph file where each line is `source destination weight` and prints the shortest paths from vertex `0`. Sample graphs live in `data/`:

```
python test.py data/example1.txt
```

```
Shortest distances from 0:
{0: 0, 1: 4, 2: 12, 3: 19, 4: 21, 5: 11, 6: 9, 7: 8, 8: 14}
spf to 0: []
spf to 1: [0]
...
```

## Project layout

```
src
|__graphs_adenpotato
   |__ __init__.py
   |__ heapq.py
   |__ sp.py
   |__ traversal.py
data/          sample graph files
test.py
README.md
pyproject.toml
```

## Contributing

`main` is protected. Do development on the `dev` branch (or a feature branch off it) and open a pull request into `main`.

## License

MIT
