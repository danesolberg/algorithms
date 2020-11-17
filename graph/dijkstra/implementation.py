class Node:
    def __init__(self, val, adjacent):
        self.val = val
        self.adjacent = adjacent

import heapq
def dijkstra(adj_list, mapping, start):
    n = len(adj_list)
    dists = [float("inf")] * n
    parents = [None] * n

    dists[mapping[start]] = 0
    pq = [(0, mapping[start])]

    while pq:
        cur_dist, cur_node = heapq.heappop(pq)
        # can push same node into pq multiple times, so only process node once (the shortest path to node).
        if cur_dist > dists[cur_node]:
            continue
        neighbors = adj_list[cur_node]
        for i, weight in neighbors:
            distance = weight + cur_dist
            if distance < dists[i]:
                dists[i] = distance
                parents[i] = cur_node
                heapq.heappush(pq, (distance, i))
    return dists


if __name__ == "__main__":
    a = Node('a', [])
    b = Node('b', [])
    c = Node('c', [])
    d = Node('d', [])
    e = Node('e', [])
    f = Node('f', [])

    a.adjacent = [(b,4), (c,6), (f,7)]  # 0
    b.adjacent = [(a,4), (d,5), (e,1), (f,3)]  # 1
    c.adjacent = [(a,6), (d,1)]  # 2
    d.adjacent = [(b,5), (c,1), (e,3)]  # 3
    e.adjacent = [(b,1), (d,3)]  # 4
    f.adjacent = [(a,7), (b,3)]  # 5

    mapping = {
        a: 0,
        b: 1,
        c: 2,
        d: 3,
        e: 4,
        f: 5
    }

    adj_list = [[(mapping[n], w) for n, w in v.adjacent] for v in [a,b,c,d,e,f]]
    print(adj_list)
    dists = dijkstra(adj_list, mapping, a)

    print(dists)