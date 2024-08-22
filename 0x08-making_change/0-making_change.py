#!/usr/bin/python3
"""
Module To Give Change
"""


def makeChange(coins, total):
    """
    Given a pile of coins of different values,
    determine the fewest number of coins needed to meet a given amount total.
    """
    coins.sort(reverse=True)  # Sort coins in descending order
    coin_count = 0
    div_half = int(total/2)
    if div_half in coins:
        return 2

    for coin in coins:
        while total >= coin:
            total -= coin
            coin_count += 1
    return coin_count if total == 0 else -1
