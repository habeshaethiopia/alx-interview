#!/usr/bin/python3
"""
minimum number of coins required
to make up a given total amount
"""


def makeChange(coins, total):
    """the function"""
    dp = [total + 1] * (total + 1)
    dp[0] = 0

    for i in range(1, total + 1):
        for j in range(0, len(coins)):
            if coins[j] <= i:
                dp[i] = min(dp[i], dp[i - coins[j]] + 1)
    return dp[-1] if dp[-1] < total else -1
