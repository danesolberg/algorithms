def merge(original, left, right):
    i, j, k = 0, 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            original[k] = left[i]
            i += 1
        else:
            original[k] = right[j]
            j += 1
        k += 1

    if i < len(left):
        original[k:] = left[i:]
    else:
        original[k:] = right[j:]


def mergesort(a):
    if len(a) > 1:
        mid = len(a) // 2
        left = a[:mid]
        right = a[mid:]

        mergesort(left)
        mergesort(right)
        merge(a, left, right)


if __name__ == '__main__':
    unsorted = [7, 2, 1, 6, 8, 5, 3, 4]
    mergesort(unsorted)
    assert unsorted == [1,2,3,4,5,6,7,8]
