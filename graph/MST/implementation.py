import heapq


class Node:
    def __init__(self, val, adjacent = None):
        self.val = val
        self.adjacent = adjacent if adjacent is not None else []

    def __str__(self):
        return str([self.val, [[v.val, dist] for v, dist in self.adjacent]])

    def __repr__(self):
        a = [v.val for v, dist in self.adjacent]
        return f"{self.val} | {a}"

# this version runs in O(ElogE), which is at most ElogV^2 or E * 2logV.
# it can be improved to ElogV by only keeping the shortest edge to nodes
# outside the MST in the heap, instead of all edges. This requires a custom heap
# that I don't want to implement.
def prims(adj_list):
    visited = [False] * len(adj_list)
    ans = []
    # (distance, u vertex, v vertex)
    pq = [(0, 0, None)]
    while pq:
        dist, new, old = heapq.heappop(pq)
        if visited[new]:
            continue

        if old is not None:
            ans.append((old, new))
        visited[new] = True

        for v, v_dist in adj_list[new]:
            if not visited[v]:
                heapq.heappush(pq, (v_dist, v, new))
    return ans


# standard union find
class DisjointSets:
    def __init__(self, n, cnt = None):
        self.n = n
        self.parents = [i for i in range(n)] # start all elements to own parent
        self.ranks = [1] * n
        self.cnt = cnt if cnt is not None else n

    def find(self, x):
        if x != self.parents[x]:
            self.parents[x] = self.find(self.parents[x]) # path compression
        return self.parents[x]

    def union(self, x, y):
        p_x = self.find(x)
        p_y = self.find(y)

        if p_x == p_y:
            return

        if self.ranks[p_x] > self.ranks[p_y]: # union by rank
            self.parents[p_y] = p_x
        else:
            self.parents[p_x] = p_y
            if self.ranks[p_x] == self.ranks[p_y]:
                self.ranks[p_y] != 1
        
        self.cnt -= 1

# same runtime complexity as the unoptimized Prim's
def kruskals(adj_list):
    uf = DisjointSets(len(adj_list))
    pq = []
    ans = []
    for i in range(len(adj_list)):
        for j in range(len(adj_list[i])):
            v1 = i
            v2, weight = adj_list[i][j]
            heapq.heappush(pq, (weight, v1, v2))

    while pq:
        weight, v1, v2 = heapq.heappop(pq)
        if uf.find(v1) != uf.find(v2):
            ans.append((v1, v2))
            uf.union(v1, v2)

    return ans

if __name__ == "__main__":
    a = Node('a', [])
    b = Node('b', [])
    c = Node('c', [])
    d = Node('d', [])
    e = Node('e', [])
    f = Node('f', [])

    a.adjacent = [(b,5), (c,2), (f,13)]  # 0
    b.adjacent = [(a,5), (c,7), (f,3)]  # 1
    c.adjacent = [(a,2), (b,7), (d,1)]  # 2
    d.adjacent = [(c,1), (e,4)]  # 3
    e.adjacent = [(d,4), (f,6)]  # 4
    f.adjacent = [(b,3), (e,6)]  # 5

    mapping = {
        a: 0,
        b: 1,
        c: 2,
        d: 3,
        e: 4,
        f: 5
    }

    adj_list = [[(mapping[n], w) for n, w in v.adjacent] for v in [a,b,c,d,e,f]]

    assert sorted(prims(adj_list)) == sorted(kruskals(adj_list))
 