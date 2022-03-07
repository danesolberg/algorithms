from collections import defaultdict


def top_sort(adj_list):
    visited = [False] * len(adj_list)
    stack = []

    for i in range(len(adj_list)):
        if not visited[i]:
            helper(adj_list, visited, stack, i)

    return stack[::-1]  # reverse to go against direction of edges. A -> B means A is a prereq for B

def helper(adj_list, visited, stack, i):
    visited[i] = True

    for adj in adj_list[i]:
        if not visited[adj]:
            helper(adj_list, visited, stack, adj)

    stack.append(i)

class Node:
    def __init__(self, val, adjacent):
        self.val = val
        self.adjacent = adjacent

def tester(graph_data):
    ADJACENCY_LIST = 1
    VERTEX_LIST = 2
    prereqs = defaultdict(list)
    if isinstance(graph_data[0], list):
        type = ADJACENCY_LIST
    elif isinstance(graph_data[0], Node):
        type = VERTEX_LIST

    for i, v in enumerate(graph_data):
        if type == 1:
            for v_adj in v:
                prereqs[v_adj].append(i)
        elif type == 2:
            for n in v.adjacent:
                prereqs[n].append(v)
        else:
            raise ValueError('invalid graph data format')

    if type == 1:
        order = top_sort(graph_data)
        for i, vertex_idx in enumerate(order):
            prereq_list = prereqs[vertex_idx]
            assert set(prereq_list) | set(order[:i]) == set(order[:i])



if __name__ == "__main__":
    a = Node('a', [])
    b = Node('b', [])
    c = Node('c', [])
    d = Node('d', [])
    e = Node('e', [])
    f = Node('f', [])

    a.adjacent = [b,d]  # 0
    b.adjacent = [c]  # 1
    c.adjacent = []  # 2
    d.adjacent = [b]  # 3
    e.adjacent = [a,b,f]  # 4
    f.adjacent = [c]  # 5

    adj_list = [
        [1,3],
        [2],
        [],
        [1],
        [0,1,5],
        [2],
    ]

    tester(adj_list)