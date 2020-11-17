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

    order = top_sort(adj_list)

    print(order)