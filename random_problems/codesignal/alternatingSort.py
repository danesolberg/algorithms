def alternatingSort(a):
    if not a:
        return True
    
    prev = a[0]
    for i in range(1,len(a)):
        div, mod = divmod(i, 2)
        if mod == 0:
            cur = a[div]
        else:
            cur = a[-1 - div]
        if cur < prev:
            return False
        prev = cur
    return True


if __name__ == "__main__":
    a = [1,3,5,6,4,2]
    print(alternatingSort(a))