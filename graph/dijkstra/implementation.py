import math
import heapq


class Node:
    def __init__(self, val, adjacent):
        self.val = val
        self.adjacent = adjacent

def dijkstra(adj_list, mapping, start, goal=None):
    n = len(adj_list)
    dists = [math.inf] * n
    parents = [None] * n
    visited = set([mapping[start]])

    dists[mapping[start]] = 0
    pq = [(0, mapping[start])]

    while pq:
        cur_dist, cur_node = heapq.heappop(pq)

        if goal and cur_node == mapping[goal]:
            return cur_dist

        visited.add(cur_node)
        neighbors = adj_list[cur_node]
        for i, weight in neighbors:
            if i not in visited:
                new_dist = weight + cur_dist
                if new_dist < dists[i]:
                    dists[i] = new_dist
                    parents[i] = cur_node
                    heapq.heappush(pq, (new_dist, i))
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

    dists = dijkstra(adj_list, mapping, a)

    print(dists)
    # no goal node
    assert dists == [0,4,6,7,5,7]
    # with goal node
    assert dijkstra(adj_list, mapping, a, f) == 7
