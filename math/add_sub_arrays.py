def add(a, b):
    carry = 0
    total = 0
    mult = 1

    while a and b:
        d1 = a.pop()
        d2 = b.pop()
        sub_total = d1 + d2 + carry
        carry, sub_total = divmod(sub_total, 10)
        sub_total *= mult
        mult *= 10
        total += sub_total
    
    while a:
        sub_total = a.pop() + carry
        carry, sub_total = divmod(sub_total, 10)
        sub_total *= mult
        mult *= 10
        total += sub_total
    while b:
        sub_total = b.pop() + carry
        carry, sub_total = divmod(sub_total, 10)
        sub_total *= mult
        mult *= 10
        total += sub_total

    total += carry * mult

    return total

def sub(a, b):
    # [1,2,3] - [3,5] = 88
    # (13-5)*1 + (11-3)*10
    # [2,3] - [3,5] = -12
    # (13-5)+(1-3)*10

    borrow = 0
    total = 0
    mult = 1

    while a and b:
        d1 = a.pop()
        d2 = b.pop()
        # borrow
        if d1 < d2:
            i = len(a)-2
            while i >= 0:
                if a[i] > 1:
                    a[i] -= 1
                    borrow = 1
                    break
                i -= 1
            if borrow == 1:
                for j in range(i+1, len(a)-1):
                    a[j] = 9

        sub_total = (d1 + borrow * 10) - d2
        borrow = 0
        sub_total *= mult
        mult *= 10
        total += sub_total

    while a:
        sub_total = a.pop() * mult
        mult *= 10
        total += sub_total
    while b:
        sub_total = b.pop() * mult
        mult *= 10
        total -= sub_total

    return total

if __name__ == "__main__":
    assert add([9,9,9], [1]) == 1000
    assert add([1,2,3], [1]) == 124
    assert add([1,2,3], [3,5]) == 158
    assert add([4,5,6], [9,7]) == 553
    assert add([1], [9]) == 10
    assert add([1], [1]) == 2
    assert add([0], [0]) == 0

    assert sub([1,2,3], [3,5]) == 88
    assert sub([2,3], [3,5]) == -12
    assert sub([1,2,3], [1,2,3]) == 0
    assert sub([0], [3,5]) == -35
    assert sub([], [3,5]) == -35
    assert sub([1,0,0,0], [1]) == 999