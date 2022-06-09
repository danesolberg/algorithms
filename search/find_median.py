from random import randint


def find_median(arr):
    n = len(arr)

    if n & 1:
        return quickselect(arr, 0, n-1, n // 2)
    else:
        a = quickselect(arr, 0, n-1, (n // 2)-1)
        b = quickselect(arr, 0, n-1, n // 2)
        return (a+b) / 2

def quickselect(arr, l, r, k):
    pi = partition(arr, l, r)
    if pi == k:
        return arr[pi]
    elif pi < k:
        return quickselect(arr, pi+1, r, k)
    else:
        return quickselect(arr, l, pi-1, k)

def partition(arr, l, r):
    pi = randint(l, r)
    arr[pi], arr[r] = arr[r], arr[pi]

    i = l
    for j in range(l, r):
        if arr[j] < arr[r]:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[r] = arr[r], arr[i]
    return i





if __name__ == "__main__":
    a1 = [5,2,6,3,1,2,7]
    assert find_median(a1) == 3

    a2 = [5,2,6,3,1,2]
    assert find_median(a2) == 2.5