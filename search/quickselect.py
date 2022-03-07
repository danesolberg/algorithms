from random import randint


def quickselect(a, start, end, k, pivot_func):
    pi = partition(a, start, end, pivot_func)
    if pi + 1 == k:
        return a[pi]
    elif pi + 1 > k:
        return quickselect(a, start, pi-1, k, pivot_func)
    else:
        return quickselect(a, pi+1, end, k, pivot_func)


def partition(a, start, end, pivot_func):
    cur = start
    if end > start:
        pi = pivot_func(a, start, end)
        a[pi], a[end] = a[end], a[pi]
        for i in range(start, end):
            if a[i] < a[end]:
                a[cur], a[i] = a[i], a[cur]
                cur += 1
        a[cur], a[end] = a[end], a[cur]
    return cur

pivot_random = lambda a, s, e: randint(s, e)

pivot_end = lambda a, s, e: e

def pivot_median_of_medians(a, start, end):
    chunks = []
    chunk_len = 50

    if (end - start + 1 < chunk_len):
        return end

    chunks = [a[i: min(end+1, i + chunk_len)] for i in range(start, end+1, chunk_len)]
    
    for chunk in chunks:
        chunk.sort()

    chunks.sort(key= lambda c: c[len(c)//2])

    middle_chunk = chunks[len(chunks)//2]

    pivot_val = middle_chunk[len(middle_chunk)//2]

    for i in range(start, end+1):
        if a[i] == pivot_val:
            return i


if __name__ == "__main__":
    array1 = [randint(0, 10**4) for _ in range(10**6)]
    array2 = [randint(0, 10**4) for _ in range(10**6)]
    array3 = [randint(0, 10**4) for _ in range(10**6)]

    sorted_array1 = sorted(array1)
    sorted_array2 = sorted(array2)
    sorted_array3 = sorted(array3)
    k = 10**5
    
    import time
    t0 = time.time()
    assert quickselect(array3, 0, len(array3)-1, k, pivot_end) == sorted_array3[k-1]
    t1 = time.time()
    print(t1 - t0)
    assert quickselect(array2, 0, len(array2)-1, k, pivot_random) == sorted_array2[k-1]
    t2 = time.time()
    print(t2-t1)
    assert quickselect(array1, 0, len(array1)-1, k, pivot_median_of_medians) == sorted_array1[k-1]
    t3 = time.time()
    print(t3-t2)

