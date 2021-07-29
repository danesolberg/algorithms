def insertionsort(a):
    for i in range(1, len(a)):
        j = i - 1
        while j >= 0 and a[j+1] < a[j]:
            a[j+1], a[j] = a[j], a[j+1]
            j -= 1


if __name__ == '__main__':
    l = [7, 2, 1, 6, 8, 5, 3, 4]
    insertionsort(l)
    assert l == [1, 2, 3, 4, 5, 6, 7, 8]
