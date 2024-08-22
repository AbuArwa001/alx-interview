#!/usr/bin/python3
"""
Module To Give Change
"""


def makeChange(coins, total):
    """
    Given a pile of coins of different values,
    determine the fewest number of coins needed to meet a given amount total.
    """
    remainder = total
    coins_count = 0
    if total == 0:
        return 0
    for coin in reversed(sorted(coins)):
        while coin <= remainder:
            remainder -= coin
            coins_count += 1
    if remainder == 0:
        return coins_count
    else:
        return -1
