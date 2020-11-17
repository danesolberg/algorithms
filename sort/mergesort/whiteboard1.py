def mergesort(arr):
    len_arr = len(arr)

    if len_arr > 1:
        # had wrong syntax for arr. forgot to reference arr when using slicing
        left = mergesort(arr[:len_arr//2])
        right = mergesort(arr[len_arr//2:])
    else:
        return arr

    new_arr = []

    while left and right:
        # i popped both immediately instead of waiting to see which was smaller
        cur_left = left[0]
        cur_right = right[0]

        if cur_left <= cur_right:
            # had to add in pops down here
            new_arr.append(left.pop(0))
        else:
            new_arr.append(right.pop(0))

    if left:
        new_arr = new_arr + left
    if right:
        new_arr = new_arr + right
    # i keep modifying new arrays instead of modifying the mutable ones passed
    return new_arr


if __name__ == '__main__':
    unsorted = [7, 2, 1, 6, 8, 5, 3, 4]
    sorted_arr = mergesort(unsorted)
    print(sorted_arr)