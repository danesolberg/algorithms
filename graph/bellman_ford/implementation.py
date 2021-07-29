from math import inf


class Node:
    def __init__(self, label, adjacent):
        self.label = label
        self.adjacent = adjacent


def bellman_ford(nodes, start):
    dists = {node: inf for node in nodes}
    dists[s] = 0

    updated = True
    while updated is True:
        updated = False

        for node in nodes:
            if dists[node] is inf:
                continue
            cur_dist = dists[node]
            for adj, weight in node.adjacent:
                new_dist = cur_dist + weight
                if new_dist < dists[adj]:
                    dists[adj] = new_dist
                    updated = True

    return dists


if __name__ == "__main__":
    a = Node('a', [])
    b = Node('b', [])
    c = Node('c', [])
    d = Node('d', [])
    e = Node('e', [])
    s = Node('s', [])

    a.adjacent = [(c, 2)]
    b.adjacent = [(a, 1)]
    c.adjacent = [(b, -2)]
    d.adjacent = [(a, -4), (c, -1)]
    e.adjacent = [(d, 1)]
    s.adjacent = [(a, 10), (e, 8)]

    dists = bellman_ford([a, b, c, d, e, s], s)
    assert (dists[s], dists[a], dists[b], dists[c], dists[d], dists[e]) == (0, 5, 5, 7, 9, 8)
