from functools import lru_cache


def levenshetin_dist_bottom_up(a, b):
    if not a:
        return len(b)
    if not b:
        return len(a)

    dp = [[0 for _ in range(len(b))] for _ in range(len(a))]
    
    for i in range(len(dp)):
        for j in range(len(dp[i])):
            if i + j == 0:
                pass
            elif i == 0:
                dp[i][j] = dp[i][j-1]
            elif j == 0:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1],dp[i-1][j-1])

            # important bit down here!
            if a[i] != b[j]:
                dp[i][j] += 1

    return dp[-1][-1]


def levenshtein_distance_top_down(a, b):
    @lru_cache(None)
    def calc_dist(i, j):
        if i < 0:
            return j+1
        if j < 0:
            return i+1

        if a[i] == b[j]:
            return calc_dist(i-1, j-1)
        else:
            return 1 + min(calc_dist(i-1,j), calc_dist(i,j-1), calc_dist(i-1,j-1))
        
    if not a:
        return len(b)
    if not b:
        return len(a)

    return calc_dist(len(a)-1, len(b)-1)


if __name__ == "__main__":
    ld_t = levenshtein_distance_top_down
    ld_b = levenshetin_dist_bottom_up
    assert ld_b('jaunt', 'bunt') == 2
    assert ld_t('jaunt', 'bunt') == 2
    assert ld_b('treck', 'eccentric') == ld_t('treck', 'eccentric') == 7
    assert ld_b('jangle', 'lucky') == ld_t('jangle', 'lucky') == 6