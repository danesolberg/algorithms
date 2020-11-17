BASE = 101

def compute_hash(string, highest_mult):
    mult = BASE**highest_mult
    h = 0
    for i in range(len(string)):
        c = string[i]
        h += ord(c) * mult
        mult //= BASE
    return h % pow(2,31)

def roll_hash(cur_hash, drop_c, add_c, highest_mult):
    return (((cur_hash - ord(drop_c)*pow(BASE,highest_mult)) * BASE) + ord(add_c)) % pow(2,31)

def compare(pattern, string, start):
    for i in range(len(pattern)):
        if pattern[i] != string[start+i]:
            return False
    return True

def contains(string, pattern):
    pat_l = len(pattern)
    pat_hash = compute_hash(pattern, pat_l-1)

    l = 0
    r = pat_l - 1
    win_pat = string[l:r+1]
    win_hash = compute_hash(win_pat, pat_l-1)
    if win_hash == pat_hash and compare(pattern, win_pat, l):
        return l
    l += 1
    r += 1
    while r < len(string):
        win_hash = roll_hash(win_hash, string[l-1], string[r], pat_l-1)
        if win_hash == pat_hash and compare(pattern, string, l):
            return l
        l += 1
        r += 1
    return -1


if __name__ == '__main__':
    string = "ababcaababcaabc"
    pat = "ababcaabc"
    
    print(contains(string, pat))
        