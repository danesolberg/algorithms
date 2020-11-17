def percolate_up(arr, i):
    while i > 0:
        parent_i = (i-1) // 2

        if arr[i] <= arr[parent_i]:
            return
        else:
            arr[i], arr[parent_i] = arr[parent_i], arr[i]
            i = parent_i

def percolate_down(arr, i):
    child_i = 2*i + 1
    cur_val = arr[i]

    while child_i < len(arr):
        max_val = cur_val
        max_i = i

        j = 0
        while j < 2 and child_i + j < len(arr):
            if arr[child_i + j] > max_val:
                max_val = arr[child_i + j]
                max_i = child_i + j
            j += 1

        if max_val == cur_val:
            return
        else:
            arr[i], arr[max_i] = arr[max_i], arr[i]
            i = max_i
            child_i = 2*i + 1

def insert(arr, val):
    arr.append(val)
    percolate_up(arr, len(arr)-1)
    
def remove(arr):
    top_val = arr[0]
    bottom_val = arr.pop()

    if arr:
        arr[0] = bottom_val
        percolate_down(arr, 0)

    return top_val

def heapify(arr):
    for i in range(len(arr) // 2 - 1, -1, -1):
        percolate_down(arr, i)

def heapsort(arr):
    heapify(arr)
    res = []
    while arr:
        top = remove(arr)
        res.append(top)
    return res[::-1]

if __name__ == '__main__':
    arr = [1,3,4,7,6,2,5]
    # heapify(arr)
    # print(arr)
    print(heapsort(arr))