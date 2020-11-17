def top_sort(adj_list):
    visited = [False] * len(adj_list)
    stack = []
    cur_path = [False] * len(adj_list) # keep track of visited nodes on current path
    for i in range(len(adj_list)):
        if not visited[i]:
            ret = helper(adj_list, visited, cur_path, stack, i)
            if ret == False: # return found cycle
                return False

    return stack[::-1]  # reverse to go against direction of edges. A -> B means A is a prereq for B

def helper(adj_list, visited, cur_path, stack, i):
    visited[i] = True
    cur_path[i] = True
    for adj in adj_list[i]:
        if cur_path[adj]: # means you hit cycle
            return False 
        if not visited[adj]:
            ret = helper(adj_list, visited, cur_path, stack, adj)
            if ret == False: # return found cycle up stack
                return False

    cur_path[i] = False # clear path as you return up the stack, for next top_sort iteration
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
        [1, 3],  # has cycle
        [0,1,5],
        [2],
    ]

    order = top_sort(adj_list)

    print(order)