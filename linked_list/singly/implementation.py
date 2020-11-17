class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, new_node):
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def prepend(self, new_node):
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def insert_after(self, cur_node, new_node):
        if not self.head:
            self.head = new_node
            self.tail = new_node
        elif cur_node is self.tail:
            # self.append(new_node)
            self.tail.next = new_node
            self.tail = new_node
        else:
            new_node.next = cur_node.next
            cur_node.next = new_node

    def remove_after(self, cur_node):
        # remove head
        if not cur_node and self.head:
            self.head = self.head.next
            # head was only node, and now its gone
            if not self.head.next:
                self.tail = None
        elif cur_node.next:
            suc_node = cur_node.next.next
            # remove next node from list
            cur_node.next = suc_node
            # if next node was tail
            if not suc_node:
                self.tail = cur_node

    def peek_front(self):
        return self.head

    def peek_back(self):
        return self.tail

    def pop_front(self):
        head = self.head
        self.remove_after(None)
        return head

    def pop_back(self):
        tail = self.tail
        prev_node = None
        cur_node = self.head
        while cur_node.next:
            prev_node = cur_node
            cur_node = cur_node.next

        self.remove_after(prev_node)
        return tail
            

if __name__ == '__main__':
    l = SinglyLinkedList()
    l.append(Node(5))
    l.append(Node(4))
    l.append(Node(3))
    l.append(Node(2))
    l.append(Node(1))

    l.pop_front()

    ptr = l.head
    s = ""
    while ptr:
        s += str(ptr.data)
        ptr = ptr.next
    print(s)