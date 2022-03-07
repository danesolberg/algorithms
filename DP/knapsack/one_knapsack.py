# knapsack problem where you can only use one item

from functools import lru_cache

def one_knapsack_bottom_up(space, items):
    items = sorted(items)

    dp = [[[] for _ in range(len(items))] for _ in range(space+1)]

    for i in range(1, len(dp)):
        for j in range(len(dp[i])):
            item = items[j]

            if j == 0:
                if item <= i:
                    dp[i][j].append(item)
                    continue
            else:
                rem = i - sum(dp[i][j-1])
                if rem >= item:
                    dp[i][j] = dp[i][j-1][:]
                    dp[i][j].append(item)
                    continue
                else:
                    if i >= item:
                        cur = sum(dp[i][j-1])
                        alt = sum(dp[i-item][j-1]) + item
                        if cur > alt:
                            dp[i][j] = dp[i][j-1][:]
                        else:
                            dp[i][j] = dp[i-item][j-1][:]
                            dp[i][j].append(item)
                    else:
                        dp[i][j] = dp[i][j-1][:]

    if dp and dp[-1]:
        return dp[-1][-1]
    else:
        return []


def one_knapsack_top_down(space, items):
    @lru_cache(None)
    def recurse(space, items_avail):
        nonlocal items

        if space == 0:
            return []
        if items_avail < 0:
            return []

        item = items[items_avail]
        space_rem = space - sum(recurse(space, items_avail-1))

        if space_rem >= item:
            return [item] + recurse(space, items_avail-1)
        else:
            if space >= item:
                cur = sum(recurse(space, items_avail-1))
                alt = sum(recurse(space - item, items_avail-1)) + item

                if cur > alt:
                    return recurse(space, items_avail-1)
                else:
                    return recurse(space - item, items_avail-1) + [item]
            else:
                return recurse(space, items_avail-1)


    items = sorted(items)

    return recurse(space, len(items)-1)


if __name__ == "__main__":
    assert one_knapsack_bottom_up(10, [3,5,1,7]) == [3,7]
    assert one_knapsack_top_down(10, [3,5,1,7]) == [3,7]
    assert one_knapsack_top_down(10, [1,1,1,1,1,1,1,1,1,1,1,1,1,1]) == [1,1,1,1,1,1,1,1,1,1]
    assert one_knapsack_top_down(10, [3,3,3,1,1,1,1,1,1,1,1,1,1,1,1,1,1]) == [1,3,3,3]

    assert one_knapsack_bottom_up(10, []) == []
    assert one_knapsack_top_down(10, []) == []

    assert one_knapsack_bottom_up(0, [1,3,5]) == []
    assert one_knapsack_top_down(0, [1,3,5]) == []

    assert one_knapsack_bottom_up(2, [2]) == [2]
    assert one_knapsack_top_down(2, [2]) == [2]