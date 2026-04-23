from sliding_window.best_time_to_buy_sell_stock import Solution


def test_best_time_to_buy_and_sell_stock() -> None:
    solution = Solution()
    assert solution.max_profit([7, 1, 5, 3, 6, 4]) == 5
    assert solution.max_profit([7, 6, 4, 3, 1]) == 0
