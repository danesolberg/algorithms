from functools import lru_cache


def get_number_of_options(
        price_of_jeans,
        price_of_shoes,
        price_of_skirts,
        price_of_tops,
        dollars
):
    @lru_cache(None)
    def backtrack(product_idx, dollars_rem):
        if product_idx == len(product_prices):
            return 1

        # num_combos = 0
        # for price in product_prices[product_idx]:
        #     if price > dollars_rem:
        #         break
        #
        #     num_combos += backtrack(product_idx+1, dollars_rem-price)
        #
        # return num_combos

        # ends up being the same problem as the counting stair traversals (number_of_traversals_staircase.py) DP problem
        return sum(backtrack(product_idx + 1, dollars_rem - price) for price in product_prices[product_idx] if
                   dollars_rem - price >= 0)


    product_prices = [
        sorted(price_of_jeans),
        sorted(price_of_shoes),
        sorted(price_of_skirts),
        sorted(price_of_tops)
    ]
    return backtrack(0, dollars)


if __name__ == "__main__":
    assert get_number_of_options(
        [2, 3],
        [4],
        [2, 3],
        [1, 2],
        10
    ) == 4

    get_number_of_options(
        list(range(1, 1000, 2)),
        list(range(1, 2000, 3)),
        list(range(20, 450)),
        list(range(1, 1000, 4)),
        300
    ) 

    print('done')

