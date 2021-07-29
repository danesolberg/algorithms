def quickselect(a, start, end, k):
    pi = partition(a, start, end)
    if pi + 1 == k:
        return a[pi]
    elif pi + 1 > k:
        return quickselect(a, start, pi-1, k)
    else:
        return quickselect(a, pi+1, end, k)


def partition(a, start, end):
    cur = start
    for i in range(start, end):
        if a[i] < a[end]:
            a[cur], a[i] = a[i], a[cur]
            cur += 1
    a[cur], a[end] = a[end], a[cur]
    return cur
