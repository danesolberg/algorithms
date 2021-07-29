def selectionsort(a):
    for i in range(len(a)):
        min_idx = i
        for j in range(i+1, len(a)):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]

if __name__ == "__main__":
    unsorted = [9,5,6,8,7,4,3,2,1]
    selectionsort(unsorted)
    assert unsorted == [1,2,3,4,5,6,7,8,9]