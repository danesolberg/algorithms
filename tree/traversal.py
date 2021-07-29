class Node:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return(f"Node: {str(self.value)}")


def preorder(root, arr):
    if root:
        arr.append(root.value)
        preorder(root.left, arr)
        preorder(root.right, arr)
    return arr


def preorder_iter(root, arr):
    if root:
        stack = [root]
        while stack:
            cur = stack.pop()
            arr.append(cur.value)
            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)
    return arr


def inorder(root, arr):
    if root:
        inorder(root.left, arr)
        arr.append(root.value)
        inorder(root.right, arr)
    return arr


def inorder_iter(root, arr):
    if root:
        stack = []
        cur = root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left

            if cur is None:
                cur = stack.pop()
                arr.append(cur.value)

            if cur:
                cur = cur.right
    return arr


def postorder(root, arr):
    if root:
        postorder(root.left, arr)
        postorder(root.right, arr)
        arr.append(root.value)
    return arr


def postorder_iter(root, arr):
    if root:
        stack = []
        cur = root
        while cur or stack:
            while cur:
                cur.visits = 0
                stack.append(cur)
                cur = cur.left

            if cur is None:
                cur = stack[-1]
                cur.visits += 1
                if cur.visits == 2:
                    arr.append(cur.value)
                    stack.pop()

            if cur and cur.visits == 2:
                cur = None
            if cur:
                cur = cur.right
        return arr


if __name__ == "__main__":
    a = Node('a', None, None)
    d = Node('d', None, None)
    f = Node('f', None, None)
    b = Node('b', a, None)
    e = Node('e', d, f)
    c = Node('c', b, e)

    assert preorder(c, []) == ['c', 'b', 'a', 'e', 'd', 'f']
    assert inorder(c, []) == ['a', 'b', 'c', 'd', 'e', 'f']
    assert postorder(c, []) == ['a', 'b', 'd', 'f', 'e', 'c']

    assert preorder(c, []) == preorder_iter(c, [])
    assert inorder(c, []) == inorder_iter(c, [])
    assert postorder(c, []) == postorder_iter(c, [])
