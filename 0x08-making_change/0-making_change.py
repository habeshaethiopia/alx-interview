#!/usr/bin/python3
"""
minimum number of coins required
to make up a given total amount
"""

from typing import List


def makeChange(coins: List[int], amount: int) -> int:
    """make changes"""
    dp = [0] + [float("inf")] * amount
    for i in range(1, amount + 1):
        for j in coins:
            if i >= j:
                dp[i] = min(dp[i - j] + 1, dp[i])

    return dp[amount] if dp[amount] != float("inf") else -1


# print(makeChange([1256, 54, 48, 16, 102], 11111))
