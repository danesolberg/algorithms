def quicksort(arr, l, r):
    if r - l > 0:
        pi = partition(arr, l, r)
        quicksort(arr, l, pi-1)
        quicksort(arr, pi+1, r)

def partition(arr, l, r):
    pval = arr[r]
    cur = l
    for i in range(l, r):
        if arr[i] <= pval:
            arr[cur], arr[i] = arr[i], arr[cur]
            cur += 1

    arr[cur], arr[r] = arr[r], arr[cur]
    return cur


if __name__ == "__main__":
    arr = [4,5,2,3,1,6]
    print(arr)
    quicksort(arr, 0, len(arr)-1)
    print(arr)
    assert arr == [1,2,3,4,5,6]