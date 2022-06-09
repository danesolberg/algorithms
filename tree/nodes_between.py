class Node:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return(f"Node: {str(self.value)}")


def nodes_between(root, start, end):
    def inorder(root):
        if root:
            if root is start and root is end:
                return 0, 2
            left, found_l = inorder(root.left)
            right, found_r = inorder(root.right)

            if found_l == 2:
                return left, 2
            if found_r == 2:
                return right, 2

            if root is start or root is end:
                path_to_other = max(left, right)
                if path_to_other >= 0:
                    return path_to_other, 2
                else:
                    return 0, 1
            elif found_l == 1 and found_r == 1:
                return left + right + 1, 2
            elif found_l == 1:
                return left + 1, 1
            elif found_r == 1:
                return right + 1, 1

        return -1, 0

    return inorder(root)[0]



if __name__ == "__main__":
    a = Node(10, None, None)
    d = Node(66, None, None)
    f = Node(99, None, None)
    b = Node(30, a, None)
    e = Node(73, d, f)
    c = Node(58, b, e)

    assert nodes_between(c, a, d) == 3
    assert nodes_between(c, a, c) == 1
    assert nodes_between(c, c, a) == 1
    assert nodes_between(c, f, d) == 1
    assert nodes_between(c, a, a) == 0
    