def partition(array, start, end):
    pivot = array[end]
    index_last_small = start

    for i in range(start, end, 1):
        if array[i] < pivot:
            array[index_last_small], array[i] = array[i], array[index_last_small]
            index_last_small += 1
    array[index_last_small], array[end] = array[end], array[index_last_small]
    return index_last_small


def QuickSort(array, start, end):
    if start < end:
        pivot_index = partition(array, start, end)
        QuickSort(array, start, pivot_index - 1)
        QuickSort(array, pivot_index + 1, end)


l = [7,2,1,6,8,5,3,4]

QuickSort(l, 0, 7)

print(l)
