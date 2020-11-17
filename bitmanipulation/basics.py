def get_bit(num, i):
    num = num >> i
    return num & 1

def set_bit(num, i):
    mask = 1 << i
    return num | mask

def clear_bit(num, i):
    mask = ~(1 << i)
    return num & mask

def clear_left(num, i):
    mask = ~(~0 << i)
    return num & mask

def clear_right(num, i):
    mask = ~0 << i + 1
    return num & mask

def swap_bits(num, i, j):
    if (num >> i) & 1 != (num >> j) & 1:
        mask = 1 << i | 1 << j
        return num ^ mask
    return num

if __name__ == "__main__":
    num = 75 # 1001011
    assert get_bit(num, 0) == 1
    assert get_bit(num, 3) == 1
    assert get_bit(num, 5) == 0
    assert get_bit(num, 13) == 0

    assert bin(set_bit(num, 5)) == '0b1101011'
    assert bin(set_bit(num, 1)) == '0b1001011'
    assert bin(set_bit(num, 2)) == '0b1001111'
    assert bin(set_bit(num, 7)) == '0b11001011'

    assert bin(clear_bit(num, 0)) == '0b1001010'
    assert bin(clear_bit(num, 6)) == '0b1011'
    assert bin(clear_bit(num, 9)) == '0b1001011'

    assert bin(clear_left(num, 3)) == '0b11'

    assert bin(clear_right(num, 3)) == '0b1000000'

    assert bin(swap_bits(num, 1, 5)) == '0b1101001'
    assert bin(swap_bits(num, 2, 5)) == '0b1001011'