def merge(original, left, right):
    i = 0
    j = 0
    k = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            original[k] = left[i]
            i += 1
        else:
            original[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        original[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        original[k] = right[j]
        j += 1
        k += 1


def MergeSort(array):
    if len(array) > 1:
        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]

        MergeSort(left)
        MergeSort(right)
        merge(array, left, right)


if __name__ == '__main__':
    unsorted = [7, 2, 1, 6, 8, 5, 3, 4]
    MergeSort(unsorted)
    assert unsorted == [1,2,3,4,5,6,7,8]
