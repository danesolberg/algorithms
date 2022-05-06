from bisect import bisect_left

class BSWrapper:
    def __init__(self, iterable, key):
        self.it = iterable
        self.key = key

    def __getitem__(self, i):
        return self.key(self.it[i])

    def __len__(self):
        return len(self.it)

class MemoryAllocator:
    def __init__(self, size):
        self.blocks = [0] * size
        self.open_index = [[0,size]]
        self.allocated_segments = {}

    def alloc(self, size):
        idx = bisect_left(BSWrapper(self.open_index, key=lambda x: x[1]), size)
        if idx == len(self.open_index):
            return -1
        starting_idx = self.open_index[idx][0]
        used_block = self.open_index[idx]
        used_block[0] += size
        used_block[1] -= size
        self.allocated_segments[starting_idx] = size
        for i in range(starting_idx, starting_idx + size):
            self.blocks[i] = 1
        return starting_idx

    def free(self, starting_idx):
        def merge_intervals():
            if len(self.open_index) > 1:
                new_index = [self.open_index[0]]
                for i in range(1, len(self.open_index)):
                    prev_e = new_index[-1]
                    cur_e = self.open_index[i]
                    if sum(prev_e) == cur_e[0]:
                        prev_e[1] = sum(cur_e)
                    else:
                        new_index.append(cur_e)
                self.open_index = new_index

        if starting_idx in self.allocated_segments:
            size = self.allocated_segments[starting_idx]
            del self.allocated_segments[starting_idx]
            idx = bisect_left(BSWrapper(self.open_index, key=lambda x: x[0]), starting_idx)
            self.open_index.insert(idx, [starting_idx, size])
            merge_intervals()
            for i in range(starting_idx, starting_idx + size):
                self.blocks[i] = 0



if __name__ == "__main__":
    mem = MemoryAllocator(100)

    assert mem.alloc(5) == 0
    assert mem.allocated_segments == {0: 5}
    assert mem.alloc(45) == 5
    assert mem.allocated_segments == {0: 5, 5: 45}
    assert mem.alloc(80) == -1
    assert mem.alloc(51) == -1
    assert mem.alloc(50) == 50
    mem.free(0)
    mem.free(50)
    assert mem.blocks == [0] * 5 + [1] * 45 + [0] * 50
    assert mem.allocated_segments == {5: 45}
    mem.free(5)
    assert mem.blocks == [0] * 100
    assert mem.allocated_segments == {}
