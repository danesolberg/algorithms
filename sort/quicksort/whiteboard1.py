def _partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low,high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)


def quicksort(arr, low, high):
    if low < high:
        pi = _partition(arr, low, high)
        quicksort(arr, low, pi-1)
        quicksort(arr, pi+1, high)


if __name__ == '__main__':
    l = [7,2,1,6,8,5,3,4]

    quicksort(l, 0, 7)

    print(l)