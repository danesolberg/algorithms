from order_traversal import create_tree


def iterative_dfs_traversal(root, order):
    stack = [(0, root)]
    res = []
    while stack:
        cnt, cur_node = stack.pop()
        if not cur_node:
            continue

        if cnt == 0:
            if order == "preorder":
                res.append(cur_node.value)

            stack.append((cnt+1, cur_node))
            stack.append((0, cur_node.left))
        elif cnt == 1:
            if order == "inorder":
                res.append(cur_node.value)

            stack.append((cnt+1, cur_node))
            stack.append((0, cur_node.right))
        elif cnt == 2:
            if order == "postorder":
                res.append(cur_node.value)
        
    return res


if __name__ == "__main__":
    tree = create_tree()
    assert iterative_dfs_traversal(tree, "preorder") == ['c', 'b', 'a', 'e', 'd', 'f']
    assert iterative_dfs_traversal(tree, "inorder") == ['a', 'b', 'c', 'd', 'e', 'f']
    assert iterative_dfs_traversal(tree, "postorder") == ['a', 'b', 'd', 'f', 'e', 'c']