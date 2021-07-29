def is_anagram(s1, s2):
    if len(s1) != len(s2):
        return False
    xor = 0

    for i in range(len(s1)):
        xor ^= ord(s1[i]) ^ ord(s2[i])

    return xor == 0


if __name__ == "__main__":
    print(is_anagram('aa', 'bb'))