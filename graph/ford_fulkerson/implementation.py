from collections import deque
from math import inf

# since this used BFS, it's actually Edmonds-Karp at O(V * E^2)
def ford_fulkerson(g, s, t):
    max_flow = 0
    path = bfs(g, s, t)

    while path:
        flow = inf
        for i in range(1, len(path)):
            flow = min(flow, g[path[i-1]][path[i]])

        max_flow += flow
        for i in range(1, len(path)):
            g[path[i-1]][path[i]] -= flow
            g[path[i]][path[i-1]] += flow

        path = bfs(g, s, t)

    return max_flow


def bfs(g, s, t):
    par = {}
    visited = set()
    q = deque([s])
    while q:
        cur = q.popleft()
        if cur == t:
            path = []
            while cur:
                path.append(cur)
                cur = par[cur]
            return path[::-1]

        for node, cap in enumerate(g[cur]):
            if cap > 0 and node not in visited:
                q.append(node)
                visited.add(node)
                par[node] = cur

    return []


if __name__ == "__main__":
    graph = [
                [0, 16, 13,  0,  0,  0],
                [0,  0, 10, 12,  0,  0],
                [0,  4,  0,  0, 14,  0],
                [0,  0,  9,  0,  0, 20],
                [0,  0,  0,  7,  0,  4],
                [0,  0,  0,  0,  0,  0]
            ]

    print(ford_fulkerson(graph, 0, 5))