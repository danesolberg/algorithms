class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def inorder_dfs_iter(root):
    s = [(0, root)]
    res = []
    while s:
        cur_status, cur_node = s.pop()

        if cur_status == 0:
            # preorder
            # res.append(cur_node.val)
            s.append((1, cur_node))
            if cur_node.left:
                s.append((0, cur_node.left))
                continue
        elif cur_status == 1:
            # inorder
            res.append(cur_node.val)
            s.append((2, cur_node))
            if cur_node.right:
                s.append((0, cur_node.right))
                continue
        # postorder
        # else:
        #     res.append(cur_node.val)
            
    return res


def simple_dfs_iter(root):
    s = [root]
    res = []

    while s:
        cur_node = s.pop()
        res.append(cur_node.val)
        if cur_node.left:
            s.append(cur_node.left)
        if cur_node.right:
            s.append(cur_node.right)

    return res

if __name__ == "__main__":
    nodes = {}

    for i in range(1, 7):
        nodes[i] = TreeNode(i)

    nodes[4].left = nodes[2]
    nodes[4].right = nodes[5]
    nodes[2].left = nodes[1]
    nodes[2].right = nodes[3]
    nodes[5].right = nodes[6]

    assert inorder_dfs_iter(nodes[4]) == [1,2,3,4,5,6]
    assert simple_dfs_iter(nodes[4]) == [4,5,6,2,3,1]