def partition(a, start, end):
    pi = start

    for i in range(start, end):
        if a[i] < a[end]:
            a[pi], a[i] = a[i], a[pi]
            pi += 1
    a[pi], a[end] = a[end], a[pi]

    return pi


def quicksort(a, start, end):
    if start < end:
        pi = partition(a, start, end)
        quicksort(a, start, pi-1)
        quicksort(a, pi+1, end)


if __name__ == "__main__":
    a = [9,8,7,6,5,4,3,2,1]
    quicksort(a, 0, len(a)-1)
    assert a == [1,2,3,4,5,6,7,8,9]