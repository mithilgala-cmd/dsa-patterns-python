from __future__ import annotations


class Solution:
    def max_profit(self, prices: list[int]) -> int:
        best_buy = float("inf")
        best_profit = 0

        for price in prices:
            if price < best_buy:
                best_buy = price
                continue
            best_profit = max(best_profit, int(price - best_buy))

        return best_profit
