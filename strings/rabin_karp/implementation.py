P = 101
M = 10**9 + 9

def compute_hash(string, highest_mult):
    mult = P**highest_mult
    h = 0
    for i in range(len(string)):
        c = string[i]
        h += ord(c) * mult
        mult //= P
    return h % M

def roll_hash(cur_hash, drop_c, add_c, highest_mult):
    return (((cur_hash - ord(drop_c)*pow(P,highest_mult)) * P) + ord(add_c)) % M

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
    ret = []
    while r < len(string):
        win_hash = roll_hash(win_hash, string[l-1], string[r], pat_l-1)
        if win_hash == pat_hash and compare(pattern, string, l):
            ret.append(l)
        l += 1
        r += 1

    return ret or -1


if __name__ == '__main__':
    string = "ababcaababcaabc"
    pat = "abc"
    
    print(contains(string, pat))
        