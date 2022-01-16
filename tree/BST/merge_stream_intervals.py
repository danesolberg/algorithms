# https://leetcode.com/problems/merge-intervals/solution/
# given a large stream of [start, end] intervals, merge them into existing
# intervals efficiently

# create a BST of disjoint intervals
# when an interval overlaps with existing interval, merge them together
# plus any other children nodes that are now overlapping

from enum import Enum


class Status(Enum):
    ROOT = 0
    ADD_BEFORE = 1
    ADD_AFTER = 2
    SUBSUMED = 3
    MERGE_BEFORE = 4
    MERGE_AFTER = 5
    ENCOMPASS = 6


class Node:
    def __init__(self, start, end, left_child=None, right_child=None):
        self.start = start
        self.end = end
        self.left_child = left_child
        self.right_child = right_child


class StreamingIntervalTree:
    def __init__(self):
        self.root = None

    def __str__(self):
        def dfs(root):
            if root:
                dfs(root.left_child)
                ret.append(f"[{root.start},{root.end}]")
                dfs(root.right_child)

        ret = []
        dfs(self.root)
        return ", ".join(ret)

    def query(self, start, end):
        cur_node = self.root
        anchor_node = None
        status = 0

        while cur_node:
            # before anchor_node
            if end < cur_node.start:
                anchor_node = cur_node
                cur_node = cur_node.left_child
                status = 1
            # after anchor_node
            elif start > cur_node.end:
                anchor_node = cur_node
                cur_node = cur_node.right_child
                status = 2
            # subsumed by cur_node
            elif start >= cur_node.start and end <= cur_node.end:
                anchor_node = cur_node
                status = 3
                break
            # extend start of cur_node
            elif start < cur_node.start and end >= cur_node.start and end <= cur_node.end:
                anchor_node = cur_node
                status = 4
                break
            # extend end of cur_node
            elif end > cur_node.end and start <= cur_node.end and start >= cur_node.start:
                anchor_node = cur_node
                status = 5
                break
            # encompass cur_node
            elif start < cur_node.start and end > cur_node.end:
                anchor_node = cur_node
                status = 6
                break

        return anchor_node, status

    def insert(self, start, end):
        anchor_node, status = self.query(start, end)

        if status == 0:
            self.root = Node(start, end)
        elif status == 1:
            anchor_node.left_child = Node(start, end)
        elif status == 2:
            anchor_node.right_child = Node(start, end)
        elif status == 3:
            pass
        elif status == 4:
            self.merge_left(anchor_node, start)
        elif status == 5:
            self.merge_right(anchor_node, end)
        elif status == 6:
            self.merge_left(anchor_node, start)
            self.merge_right(anchor_node, end)

    def merge_left(self, cur_node, start):
        # go left
        if cur_node and start < cur_node.start:
            # returning right (went left)
            new_start, left_child = self.merge_left(cur_node.left_child, start)
            new_start = min(start, new_start)
            cur_node.start = new_start
            cur_node.left_child = left_child
            # print(new_start)
            return new_start, cur_node.left_child
        # go right
        elif cur_node and start > cur_node.end:
            # returning left (went right)
            new_start, right_child = self.merge_left(cur_node.right_child, start)
            # leave cur_node.left_child alone since it's been changed already
            cur_node.right_child = right_child
            # print(start)
            return new_start, cur_node
        # start of new interval is inside cur_node interval, so all left children are disjoint
        # and cur_node + all right children get merged
        elif cur_node:
            new_start = min(start, cur_node.start)
            # print(new_start)
            return new_start, cur_node.left_child # right child is merged (dereferenced)
        # reached end of tree
        else:
            # print(start)
            return start, None

    def merge_right(self, cur_node, end):
        # go right
        if cur_node and end > cur_node.end:
            # returning left (went right)
            new_end, right_child = self.merge_right(cur_node.right_child, end)
            new_end = max(end, new_end)
            cur_node.end = new_end
            cur_node.right_child = right_child
            return new_end, cur_node.right_child
        # go left
        elif cur_node and end < cur_node.start:
            # returning right (went left)
            new_end, left_child = self.merge_right(cur_node.left_child, end)
            # leave cur_node.right_child alone since it's been changed already
            cur_node.left_child = left_child
            return new_end, cur_node
        # end of new interval is inside cur_node interval, so all right children are disjoint
        # and cur_node + all left children get merged
        elif cur_node:
            new_end = max(end, cur_node.end)
            return new_end, cur_node.right_child # left child is merged (dereferenced)
        # reached end of tree
        else:
            return start, None


if __name__ == "__main__":
    stream = [
        [30,33],
        [10,14],
        [5,6],
        [6,11],
        [17,18],
        [1,1],
        [4,4],
        [3,3],
        [7,7],
        [8,8],
        [15,16],
        [20,25],
        [19,19],
        [50,58],
        [2,14],
        [22,31],
        [19,50],
        [5, 100]
    ]

    tree = StreamingIntervalTree()

    for i in stream:
        start = i[0]
        end = i[1]
        tree.insert(start, end)

    print(str(tree))

