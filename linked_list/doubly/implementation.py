class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, new_node):
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def prepend(self, new_node):
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

    def insert_after(self, cur_node, new_node):
        if not self.head:
            self.head = new_node
            self.tail = new_node
        elif cur_node is self.tail:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        else:
            suc_node = cur_node.next.next
            new_node.next = suc_node
            new_node.prev = cur_node
            cur_node.next = new_node
            suc_node.prev = new_node

    def remove_node(self, cur_node):
        suc_node = cur_node.next
        pred_node = cur_node.prev

        if pred_node:
            pred_node.next = suc_node
        if suc_node:
            suc_node.prev = pred_node
        if cur_node is self.head:
            self.head = suc_node
        if cur_node is self.tail:
            self.tail = pred_node

    def remove_index(self, index):
        i = 0
        cur_node = self.head
        while i <= index and cur_node:
            cur_node = cur_node.next
            i += 1
        
        if i == index:
            self.remove_node(cur_node)