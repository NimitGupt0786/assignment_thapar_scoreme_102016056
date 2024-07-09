
### 2. `main.py`

"""python"""
"""
Assignment: Implement the most efficient algorithm to solve the given problem.

Problem Statement:
You are given a Directed Acyclic Graph (DAG) with `n` nodes, numbered from `0` to `n-1`.
The graph is represented as an adjacency list where `graph[i]` is a list of tuples `(j, w)`,
representing an edge from node `i` to node `j` with weight `w`. Your task is to find the longest
path in the graph starting from any node.

Function Signature:
def longest_path(graph: list) -> int:

Parameters:
- graph (list): A list of lists, where `graph[i]` contains tuples `(j, w)` representing an edge
  from node `i` to node `j` with weight `w`.

Returns:
- int: The length of the longest path in the graph.

Example:
>>> graph = [
...     [(1, 3), (2, 2)],
...     [(3, 4)],
...     [(3, 1)],
...     []
... ]
>>> longest_path(graph)
7
"""
from collections import defaultdict, deque

# Helper function to perform topological sort
def topological_sort(graph):
    """
        Perform topological sorting using Kahn's algorithm.
    """
    in_degree = defaultdict(int)
    for u in range(len(graph)):
        for v, _ in graph[u]:
            in_degree[v] += 1

    zero_in_degree_queue = deque([u for u in range(len(graph)) if in_degree[u] == 0])
    topo_order = []

    while zero_in_degree_queue:
        u = zero_in_degree_queue.popleft()
        topo_order.append(u)
        for v, _ in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                zero_in_degree_queue.append(v)

    return topo_order

# Function to calculate longest path using topological sort
def calculate_longest_path(graph, topo_order):
    """
        Calculate the longest path in the DAG using dynamic programming.
    """
    # Initialize distances from the source
    n = len(graph)
    dist = [-float('inf')] * n
    dist[0] = 0  # Start from node 0

    # Process vertices in topological order
    for u in topo_order:
        if dist[u] != -float('inf'):  # Ensure u is reachable
            for v, weight in graph[u]:
                if dist[v] < dist[u] + weight:
                    dist[v] = dist[u] + weight

    # Find the maximum distance in dist[]
    max_distance = max(dist)
    return max_distance

def longest_path(graph: list) -> int:
    max_path_length = 0
    n = len(graph)

    for start_node in range(n):
        topo_order = topological_sort(graph)
        max_path_length = max(max_path_length, calculate_longest_path(graph, topo_order))

        # Remove edges from the start_node to explore paths starting from other nodes
        for u in range(n):
            graph[u] = [(v, w) for v, w in graph[u] if v != start_node]

    return max_path_length