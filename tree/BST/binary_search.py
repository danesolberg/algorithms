class Node:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return(f"Node: {str(self.value)}")


def BinarySearchRecursive(node, key):
    if not node:
        return None

    if node.value == key:
        return node
    elif key < node.value:
        return BinarySearchRecursive(node.left, key)
    elif key > node.value:
        return BinarySearchRecursive(node.right, key)

    return(-1)


def BinarySearchIterative(node, key):
    curNode = node
    while(curNode is not None):
        if curNode.value == key:
            return curNode
        if key < curNode.value:
            curNode = curNode.left
        elif key > curNode.value:
            curNode = curNode.right

    return None

def InOrderTraversal(node):
    if not node:
        return
    InOrderTraversal(node.left)
    print(node)
    InOrderTraversal(node.right)

def InOrderTraversalList(node):
    if node.left:
        left = InOrderTraversalList(node.left)
    else:
        left = []
    if node.right:
        right = InOrderTraversalList(node.right)
    else:
        right = []
    return left + [node.value] + right

def remove(root, key):
    par_node = None
    cur_node = root

    while cur_node:
        if cur_node.value == key:
            if not cur_node.left and not cur_node.right: # leaf node
                if not par_node: # cur_node is root
                    cur_node = None
                elif par_node.left == cur_node:
                    par_node.left = None
                else:
                    par_node.right = None
            elif cur_node.left and not cur_node.right: # internal node with only left child
                if not par_node: # cur_node is root
                    cur_node = cur_node.left
                elif par_node.left == cur_node:
                    par_node.left = cur_node.left
                else:
                    par_node.right = cur_node.left
            elif not cur_node.left and cur_node.right: # internal node with only right child
                if not par_node: # cur_node is root
                    cur_node = cur_node.right
                elif par_node.left == cur_node:
                    par_node.left = cur_node.right
                else:
                    par_node.right = cur_node.right
            else: # internal node with two children
                suc_node = cur_node.right
                while suc_node.left: # find the successor node of the cur_node
                    suc_node = suc_node.left
                suc_data = suc_node.value # copy the suc_node's data
                remove(cur_node.right, suc_data) # remove the suc_node from the BST
                cur_node.value = suc_data # move the suc_node's data into the original removed node's (cur_node) spot
            return
        elif key > cur_node.value: # search right
            par_node = cur_node
            cur_node = cur_node.right
        else: # search left
            par_node = cur_node
            cur_node = cur_node.left
    return

def insert(root, key):
    if not root:
        root = Node(key, None, None)
    else:
        cur_node = root
        while cur_node: # since node always inserted at bottom, just traverse down
            if key < cur_node.value:
                if not cur_node.left:
                    cur_node.left = Node(key, None, None)
                    break
                else:
                    cur_node = cur_node.left
            else:
                if not cur_node.right:
                    cur_node.right = Node(key, None, None)
                    break
                else:
                    cur_node = cur_node.right

if __name__ == "__main__":
    a = Node(10, None, None)
    d = Node(66, None, None)
    f = Node(99, None, None)
    b = Node(30, a, None)
    e = Node(73, d, f)
    c = Node(58, b, e)

    print(InOrderTraversal(c))
    # print(BinarySearchRecursive(c, 10))
    # print(BinarySearchIterative(c, 10))

    remove(c, 73)
    insert(c, 6)
    print(InOrderTraversal(c))