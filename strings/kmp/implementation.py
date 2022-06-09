def kmp(string, pat):
    def precompute_suffix_arr():
        suffix_arr = [0] * len(pat)
        i = 0
        j = 1

        while j < len(pat):
            if pat[i] != pat[j]:
                i = suffix_arr[i]
                j += 1
            else:
                suffix_arr[j] = i+1
                i += 1
                j += 1
        return suffix_arr

    def compare(i, j):
        while i < len(string) and j < len(pat):
            # print(string[i],pat[j])
            if string[i] == pat[j]:
                i += 1
                j += 1
            else:
                return j, False

        if j == len(pat):
            return j-1, True
        else:
            return j, False

    suffix_arr = precompute_suffix_arr()
    found_indices = []
    i, j = 0, 0
    skip_dist = 0
    while i < len(string):
        if string[i] == pat[j]:
            k, found = compare(i+1, j+1)
            if found:
                found_indices.append(i - skip_dist)
                i = i + (k-j) + 1
            else:
                i = i + (k-j)
            skip_dist = suffix_arr[k]
            j = suffix_arr[k]
        else:
            i += 1
            j = suffix_arr[j]

    return found_indices




if __name__ == "__main__":
    s = "aabcabcabd"
    p = "abcab"

    print(kmp(s, p))