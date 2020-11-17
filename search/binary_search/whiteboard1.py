def binary_search(arr, l, r, v):
    if r >= l:
        mid = l + (r - l) // 2

        if arr[mid] == v:
            return mid
        elif arr[mid] > v:
            return binary_search(arr, l, mid-1, v)
        else:
            return binary_search(arr, mid+1, r, v)
    else:
        return -1

if __name__ == '__main__':
    l = [7,2,1,6,8,5,3,4]

    l.sort()

    print(binary_search(l, 0, 7, 5))