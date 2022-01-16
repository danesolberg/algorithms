class MaxHeap:
    def __init__(self):
        self.heap_array = []

    def __str__(self):
        return str(self.heap_array)

    def percolate_up(self, node_index):
        while node_index > 0:
            parent_index = (node_index - 1) // 2

            if self.heap_array[node_index] <= self.heap_array[parent_index]:
                return
            else:
                self.heap_array[node_index], self.heap_array[parent_index] = \
                    self.heap_array[parent_index], self.heap_array[node_index]

                node_index = parent_index

    def percolate_down(self, node_index, cutoff_size):
        child_index = 2 * node_index + 1
        cur_value = self.heap_array[node_index]

        while child_index < cutoff_size:
            max_value = cur_value  # init max child val to parent val, to later know if any child > parent
            max_index = node_index
            i = 0
            while i < 2 and child_index + i < cutoff_size:
                if self.heap_array[child_index + i] > max_value:
                    max_value = self.heap_array[child_index + i]
                    max_index = child_index + i
                i += 1

            if max_value == cur_value:
                return  # parent is greater than both children
            else:
                self.heap_array[node_index], self.heap_array[max_index] = \
                    self.heap_array[max_index], self.heap_array[node_index]
                node_index = max_index
                child_index = 2 * node_index + 1

    def insert(self, value):
        self.heap_array.append(value)
        self.percolate_up(len(self.heap_array) - 1)

    def remove(self):
        max_value = self.heap_array[0]

        bottom_value = self.heap_array.pop()
        if len(self.heap_array) > 0:
            self.heap_array[0] = bottom_value
            self.percolate_down(0, len(self.heap_array))

        return max_value

    def heapify(self, arr):
        self.heap_array = arr[:]
        # start at last parent node, since nothing after can sift down
        # always (len // 2) - 1
        # percolate down is most expensive at top of heap (in worst case),
        # so start at the bottom to save worst case cost (O(n))
        for i in range(len(self.heap_array) // 2 - 1, -1, -1):
            self.percolate_down(i, len(self.heap_array))

    def heap_sort(self):
        # O(nlogn) because we sift down O(logn) from the top n times
        for i in range(len(self.heap_array)-1, 0, -1):
            self.heap_array[0], self.heap_array[i] = self.heap_array[i], self.heap_array[0]
            self.percolate_down(0, i)


if __name__ == "__main__":
    heap = MaxHeap()
    heap.heapify([1,3,4,7,6,2,5])
    heap.heap_sort()
    print(heap.heap_array)

    # for i in range(1, 8):
    #     heap.insert(i)
    #     # print(heap)

    # # for _ in range(7):
    # #     n = heap.remove()
    # #     print(n)

    # heap.heap_sort()
    # print(heap.heap_array)