import math
from collections import deque
from itertools import chain
from time import time
from random import randint

# same O(V * E) runtime, but constant factors faster. space = O(V)
def SPFA(n, adj_list, source):
    dists = [math.inf] * n
    dists[source] = 0
    q = deque([0])
    enqueued = set([0])

    while q:
        cur_node = q.popleft()
        cur_weight = dists[cur_node]

        for neighbor, weight in adj_list[cur_node]:
            new_weight = cur_weight + weight
            if new_weight < dists[neighbor]:
                if neighbor not in enqueued:
                    enqueued.add(neighbor)
                    q.append(neighbor)
                dists[neighbor] = new_weight

    return dists


def bellman_ford(n, adj_list, source):
    dists = [math.inf] * n
    dists[source] = 0

    updated = True
    while updated:
        updated = False

        for i in range(n):
            cur_dist = dists[i]
            for e, w in adj_list[i]:
                new_dist = cur_dist + w
                if new_dist < dists[e]:
                    dists[e] = new_dist
                    updated = True

    return dists

if __name__ == "__main__":
    n = 4
    adj_list = {
        0: [(1, 200), (2, 100), (3, 500)],
        1: [(2, -150)],
        2: [(3, 100)],
        3: [(0, 50), (1, 300)]
    }

    assert SPFA(n, adj_list, 0) == [0, 200, 50, 150]

    ts1 = time()
    for _ in range(100000):
        SPFA(n, adj_list, randint(0, n-1))
    ts2 = time()
    print("SPFA: ", ts2-ts1)

    ts1 = time()
    for _ in range(100000):
        bellman_ford(n, adj_list, randint(0, n-1))
    ts2 = time()
    print("BF: ", ts2-ts1)