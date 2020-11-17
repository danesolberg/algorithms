def insertion_sort(arr):
    for i in range(1, len(arr)):
        val = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > val:
            arr[j+1] = arr[j]
            j -= 1
        # this needs to be j+1, not just j, since the pointer above moves 1 step ahead of the hole
        arr[j+1] = val

if __name__ == '__main__':
    l = [7,2,1,6,8,5,3,4]

    insertion_sort(l)

    print(l)