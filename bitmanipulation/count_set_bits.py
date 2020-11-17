def count(num):
    if num < 0:
        raise ValueError
    count = 0
    while num:
        count += num & 1
        num >>= 1
    return count


if __name__ == "__main__":
    num = 75 # 1001011
    assert count(num) == 4