from collections import deque
from math import inf

# since this used BFS, it's actually Edmonds-Karp at O(V * E^2)
# while a path exists between start and end nodes, across either the normal graph
# or the residual graph (flowing in opposite direction of original capacities),
# find the capacity of that path and 1) increment max flow, 2) augment the
# primary and residual graphs.  Once no path exists with non-zero capacity, 
# the algorithm ends
def ford_fulkerson(g, s, t):
    max_flow = 0
    path = bfs(g, s, t)

    while path:
        flow = inf
        # the max possible flow down a path equals the minimum capacity at any
        # edge of the path
        for i in range(1, len(path)):
            flow = min(flow, g[path[i-1]][path[i]])

        max_flow += flow
        for i in range(1, len(path)):
            g[path[i-1]][path[i]] -= flow
            g[path[i]][path[i-1]] += flow

        path = bfs(g, s, t)

    return max_flow


def bfs(graph, start, end):
    # track parent node of each node
    # in this case, only tracking the [parent] node that first led us to a node
    # even if multiple paths to a node exist. Shouldn't matter because the order
    # of flow maximizing won't change final max flow number.
    par = {}
    visited = set([start])
    q = deque([start])
    while q:
        cur = q.popleft()
        if cur == end:
            path = []
            while cur is not None:
                path.append(cur)
                cur = par.get(cur, None)
            return path[::-1]

        # index of list is implicitly the node number
        # each element of list is the capacity
        for node, remaining_capacity in enumerate(graph[cur]):
            if remaining_capacity > 0 and node not in visited:
                q.append(node)
                visited.add(node)
                # track the previous node [parent] that first led us to this node
                par[node] = cur

    return []


if __name__ == "__main__":
    # each element n at index i,j of matrix represents the flow capacity n from
    # node i to node j
    graph = [
                [0, 16, 13,  0,  0,  0],
                [0,  0, 10, 12,  0,  0],
                [0,  4,  0,  0, 14,  0],
                [0,  0,  9,  0,  0, 20],
                [0,  0,  0,  7,  0,  4],
                [0,  0,  0,  0,  0,  0]
            ]

    print(ford_fulkerson(graph, 0, 5))