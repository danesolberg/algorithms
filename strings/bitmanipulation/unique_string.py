def is_unique(s):
    bit_mask = 0

    for c in s:
        if bit_mask & 1 << (ord(c) - ord('a')) == 0:
            bit_mask = bit_mask | 1 << (ord(c) - ord('a'))
        else:
            return False
    return True


if __name__ == "__main__":
    assert is_unique("abcdef") is True
    assert is_unique("a") is True
    assert is_unique("aa") is False
    assert is_unique("abcdefefef") is False
    assert is_unique("abbc") is False
    assert is_unique("abcdefgg") is False
    assert is_unique("abcdefghijklmnopqrstuvwxyz") is True
    assert is_unique("abcdefghijklmnopqrstuvwxyzz") is False

