def bfs_recursion(queue):
    if queue:
        node = queue.dequeue()
        print(node.val)
        for n in node.adjacent:
            if not n.visited:
                n.visited = True
                queue.enqueue(n)
        bfs_recursion(queue)

def bfs(root):
    q = Queue()
    root.visited = True
    q.enqueue(root)

    while q:
        node = q.dequeue()
        print(node.val)
        for n in node.adjacent:
            if not n.visited:
                n.visited = True
                q.enqueue(n)

class Node:
    def __init__(self, val, adjacent):
        self.val = val
        self.adjacent = adjacent
        self.visited = False

class Element:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def __bool__(self):
        return True if self.head else False

    def dequeue(self):
        if self.head:
            res = self.head
            if self.head is self.tail:
                self.tail = None
            self.head = self.head.next
            return res.data
        else:
            return None

    def enqueue(self, node):
        e = Element(node)
        if not self.head:
            self.head = e
            self.tail = e
        else:
            self.tail.next = e
            self.tail = e

if __name__ == "__main__":
    a = Node('a', [])
    b = Node('b', [])
    c = Node('c', [])
    d = Node('d', [])
    e = Node('e', [])
    f = Node('f', [])
    g = Node('g', [])

    a.adjacent = [b,c,d]
    b.adjacent = [a,c,g]
    c.adjacent = [a,b,d,f]
    d.adjacent = [a,c,e]
    e.adjacent = [d,f]
    f.adjacent = [c,e,g]
    g.adjacent = [b,f]

    # q = Queue()
    # q.enqueue(a)
    # a.visited = True
    # bfs_recursion(q)
    bfs(a)
    