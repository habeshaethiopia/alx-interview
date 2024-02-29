#!/usr/bin/python3
"""
minimum number of coins required
to make up a given total amount
"""
import sys


def makeChange(coins, amount):
    """
    :type coins: list of int
    :type amount: int
    :rtype: int
    """
    if amount < 1:
        return 0

    return coin_change(coins, amount, [0] * (amount + 1))


def coin_change(coins, remainder, cache):
    """
    Minimum coins to make change for a negative amount is -1.
    This is just a base case we arbitrarily define.
    """
    if remainder < 0:
        return -1

    """
        The minimum coins needed to make change for 0 is always 0
        coins no matter what coins we have.
        """
    if remainder == 0:
        return 0

    # We already have an answer cached. Return it.
    if cache[remainder] != 0:
        return cache[remainder]

    # No answer yet. Try each coin as the last coin in the change that
    # we make for the amount
    system_max = sys.maxsize
    minimum = system_max
    for coin in coins:
        change_result = coin_change(coins, remainder - coin, cache)

        """
            If making change was possible (changeResult >= 0) and
            the change result beats our present minimum, add one to
            that smallest value

            We accept that coin as the last coin in our change making
            sequence up to this point since it minimizes the coins we
            need
            """
        if change_result >= 0 and change_result < minimum:
            minimum = 1 + change_result

    """
        If no answer is found (minimum == max value) then the
        sub problem answer is just arbitrarily made to be -1, otherwise
        the sub problem's answer is "minimum"
        """
    cache[remainder] = -1 if (minimum == system_max) else minimum

    return cache[remainder]


# print(makeChange([1,2,3], 10))
