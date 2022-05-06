from collections import deque


class Node:
    def __init__(self, val, neighbors=None):
        self.val = val
        self.neighbors = neighbors or []

    def __repr__(self):
        return f"Node: {self.val}"

def bfs(vertex_list):
    visited = set()
    ret = []
    # accounts for case of multiple connected components
    # essentially does BFS for each connected components in graph
    for node in vertex_list:
        if node not in visited:
            visited.add(node)

            q = deque([node])
            while q:
                cur = q.popleft()
                ret.append(cur.val)
                for n in cur.neighbors:
                    if n not in visited:
                        visited.add(n)
                        q.append(n)

    return ret

def bfs_array(vertex_list):
    visited = set()
    ret = []
    for node in vertex_list:
        if node not in visited:
            visited.add(node)

            q = [node]
            next_q = []
            while q:
                for cur in q:
                    ret.append(cur.val)
                    for n in cur.neighbors:
                        if n not in visited:
                            visited.add(n)
                            next_q.append(n)
                q, next_q = next_q, q
                next_q.clear()

    return ret



if __name__ == "__main__":
    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')
    e = Node('e')
    f = Node('f')
    g = Node('g')

    # undirected graph
    a.neighbors = [b, c]
    b.neighbors = [a, c, d]
    c.neighbors = [a, b]
    d.neighbors = [b, e, f]
    e.neighbors = [d, g]
    f.neighbors = [d, g]
    g.neighbors = [e, f]

    assert bfs([a,b,c,d,e,f,g]) == ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    assert bfs([d,g,f,c,a,b,e]) == ['d', 'b', 'e', 'f', 'a', 'c', 'g']

    assert bfs([d,g,f,c,a,b,e]) == bfs_array([d,g,f,c,a,b,e])

    # directed graph
    a.neighbors = [b, c]
    b.neighbors = [d]
    c.neighbors = [b]
    d.neighbors = [e, f]
    e.neighbors = [g]
    f.neighbors = [g]
    g.neighbors = []

    assert bfs([a,b,c,d,e,f,g]) == ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    assert bfs([d,g,f,c,a,b,e]) == ['d', 'e', 'f', 'g', 'c', 'b', 'a']