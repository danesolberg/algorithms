class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def push(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def pop(self):
        node = self.head
        self.head = self.head.next
        return node.data

    def peek(self):
        return self.head.data

    def is_empty(self):
        return not self.head


if __name__ == '__main__':
    stack = Stack()
    stack.push(3)
    stack.push(2)
    stack.push(1)

    assert stack.pop() == 1
    assert stack.pop() == 2
    assert stack.pop() == 3
    print('pass')