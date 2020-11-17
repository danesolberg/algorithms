from functools import wraps
from math import ceil

class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None

class ChainingHashTable:
    def __init__(self, init_cap=10):
        self.table = [None] * init_cap
        self.count = 0

    def _load_balance(self):
        return self.count / len(self.table)

    def _resize(self, factor):
        new_table = [None] * max(ceil(len(self.table) * factor), 1)
        for node_to_move in self.table:
            while node_to_move:
                suc_node_to_move = node_to_move.next
                node_to_move.next = None
                bucket_idx = hash(node_to_move.key) % len(new_table)
                cur_node = new_table[bucket_idx]
                
                if cur_node is None:
                    new_table[bucket_idx] = node_to_move
                else:
                    while True:
                        if not cur_node.next:
                            break
                        else:
                            cur_node = cur_node.next
                    cur_node.next = node_to_move
                node_to_move = suc_node_to_move
        self.table = new_table

    def analyze(func):
        @wraps(func)
        def func_wrapper(inst, *args, **kwargs):
            retval = func(inst, *args, **kwargs)
            lb = inst._load_balance()
            if lb > 1:
                inst._resize(2)
            elif lb < 0.25:
                inst._resize(0.5)
            return retval
        return func_wrapper

    @analyze
    def insert(self, key, val):
        bucket_idx = hash(key) % len(self.table)
        cur_node = self.table[bucket_idx]
        
        if cur_node is None:
            self.table[bucket_idx] = ListNode(key, val)
            self.count += 1
            return

        while True:
            if cur_node.key == key:
                cur_node.val = val
                return
            if not cur_node.next:
                break
            else:
                cur_node = cur_node.next
        cur_node.next = ListNode(key, val)
        self.count += 1

    def search(self, key):
        bucket_idx = hash(key) % len(self.table)
        cur_node = self.table[bucket_idx]

        if cur_node is None:
            return None

        while True:
            if cur_node.key == key:
                return cur_node.val
            if not cur_node.next:
                return None
            else:
                cur_node = cur_node.next

    @analyze
    def remove(self, key):
        bucket_idx = hash(key) % len(self.table)
        cur_node = self.table[bucket_idx]

        if cur_node is None:
            return

        pred_node = None
        while True:
            if cur_node.key == key:
                if not pred_node:
                    self.table[bucket_idx] = cur_node.next
                else:
                    pred_node.next = cur_node.next
                self.count -= 1

            if not cur_node.next:
                return
            pred_node, cur_node = cur_node, cur_node.next


class EmptyBucket:
    pass

from collections import namedtuple
class OpenAddressingHashTableBase:
    EMPTY_SINCE_START = EmptyBucket()
    EMPTY_AFTER_REMOVAL = EmptyBucket()
    Item = namedtuple('Item', ['key', 'val'])

    def __init__(self, init_cap=10):
        self.table = [OpenAddressingHashTableBase.EMPTY_SINCE_START] * init_cap

    def hash(self, key, i):
        raise NotImplementedError()

    def insert(self, key, val):
        for i in range(len(self.table)):
            bucket_idx = self.hash(key, i) % len(self.table)

            if type(self.table[bucket_idx]) is EmptyBucket:
                self.table[bucket_idx] = OpenAddressingHashTableBase.Item(key, val)
                return True
            elif self.table[bucket_idx].key == key:
                self.table[bucket_idx] = OpenAddressingHashTableBase.Item(key, val)
                return True
        return False

    def remove(self, key):
        for i in range(len(self.table)):
            bucket_idx = self.hash(key, i) % len(self.table)

            if self.table[bucket_idx] == OpenAddressingHashTableBase.EMPTY_SINCE_START:
                return

            if not type(self.table[bucket_idx]) is EmptyBucket and self.table[bucket_idx].key == key:
                self.table[bucket_idx] = OpenAddressingHashTableBase.EMPTY_AFTER_REMOVAL
                return

    def search(self, key):
        for i in range(len(self.table)):
            bucket_idx = self.hash(key, i) % len(self.table)

            if self.table[bucket_idx] == OpenAddressingHashTableBase.EMPTY_SINCE_START:
                return None

            if not type(self.table[bucket_idx]) is EmptyBucket and self.table[bucket_idx].key == key:
                return self.table[bucket_idx].val
        return None
            
class LinearProbingHashTable(OpenAddressingHashTableBase):
    def hash(self, key, i):
        return hash(key) + i

class QuadraticProbingHashTable(OpenAddressingHashTableBase):
    def hash(self, key, i):
        return hash(key) + i**2

if __name__ == '__main__':
    hm = ChainingHashTable()
    assert hm.insert('test', 'test val') == None
    assert hm.insert(5, '5 val') == None
    assert hm.search(5) == '5 val'
    assert hm.insert(5, 'updated') == None
    assert hm.search(5) == 'updated'
    assert hm.search('test') == 'test val'
    assert hm.search('foo') == None
    assert hm.remove(5) == None
    assert hm.remove('test') == None
    assert hm.search('test') == None
    assert hm.remove('bar') == None
    for i in range(1000):
        hm.insert(i, i)
    assert hm.count == 1000
        
    lp = LinearProbingHashTable()
    lp.insert(1, '1 val')
    lp.insert(2, '2 val')
    lp.insert(3, '3 val')
    lp.insert(4, '4 val')
    lp.insert(5, '5 val')
    lp.insert(11, '11 val')
    assert lp.search(1) == '1 val'
    assert lp.search(5) == '5 val'
    assert lp.search(11) == '11 val'
    assert lp.search(6) == None
    assert [item.val if type(item) == OpenAddressingHashTableBase.Item else item for item in lp.table] == [lp.EMPTY_SINCE_START, '1 val', '2 val', '3 val', '4 val', '5 val', '11 val', lp.EMPTY_SINCE_START, lp.EMPTY_SINCE_START, lp.EMPTY_SINCE_START]
    lp.remove(3)
    lp.insert(21, '21 val')
    assert [item.val if type(item) == OpenAddressingHashTableBase.Item else item for item in lp.table] == [lp.EMPTY_SINCE_START, '1 val', '2 val', '21 val', '4 val', '5 val', '11 val', lp.EMPTY_SINCE_START, lp.EMPTY_SINCE_START, lp.EMPTY_SINCE_START]

    qp = QuadraticProbingHashTable()
    qp.insert(1, '1 val')
    qp.insert(11, '11 val')
    qp.insert(21, '21 val')
    qp.insert(31, '31 val')
    qp.insert(41, '41 val')
    assert [item.val if type(item) == OpenAddressingHashTableBase.Item else item for item in qp.table] == ['31 val', '1 val', '11 val', qp.EMPTY_SINCE_START, qp.EMPTY_SINCE_START, '21 val', qp.EMPTY_SINCE_START, '41 val', qp.EMPTY_SINCE_START, qp.EMPTY_SINCE_START]

    print('tests passed')


