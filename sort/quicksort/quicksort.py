from random import randint

# lomuto partition: relatively high swaps O(n^2), but Θ(nlogn)
# more common and well-known
def lomuto_partition(array, start, end):
    pivot = array[end]
    offset_left_side = start

    for i in range(start, end, 1):
        if array[i] < pivot:
            array[offset_left_side], array[i] = array[i], array[offset_left_side]
            offset_left_side += 1
    array[offset_left_side], array[end] = array[end], array[offset_left_side]
    return offset_left_side


# hoare partition: fewer swaps, but same complexity
# somewhat esoteric
# Hoare's partition is more efficient than Lomuto's partition because 
# it does three times fewer swaps on average, and creates efficient 
# partitions even when all values are equal.
def hoare_partition(array, start, end):
    pivot = array[start]
    left = start - 1
    right = end + 1

    while True:
        while True:
            left += 1
            if array[left] >= pivot:
                break
        while True:
            right -= 1
            if array[right] <= pivot:
                break
        if left >= right:
            # the right pos is moving left, so this returns the partition index
            # at which all elements <= the partition index are strictly
            # less than the pivot
            # *** UNLESS *** the pivot at array[0] is already the minimal value
            # in the subarray, in which case the pivot is at index 0 and the
            # partition index in (unmoved) at index 0
            return right
        array[left], array[right] = array[right], array[left]
    

def QuickSort(array, start, end, _partition_func=lomuto_partition):
    if start < end:
        pivot_index = _partition_func(array, start, end)
        if _partition_func == lomuto_partition:
            QuickSort(array, start, pivot_index - 1, _partition_func)
        # hoare's partition does not ensure that the element at the partition
        # index is in the correct sorted position, so we need to include it
        # in the recursion
        elif _partition_func == hoare_partition:
            QuickSort(array, start, pivot_index, _partition_func)
        else:
            raise ValueError('invalid partition function')
        QuickSort(array, pivot_index + 1, end, _partition_func)


if __name__ == "__main__":
    for _ in range(1000):
        l = [randint(0, 5000) for _ in range(100)]
        s = sorted(l)
        h = l[:]
        QuickSort(l, 0, len(l)-1, lomuto_partition)
        assert l == s
        QuickSort(h, 0, len(l)-1, hoare_partition)
        assert h == s
