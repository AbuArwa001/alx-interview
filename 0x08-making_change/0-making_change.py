#!/usr/bin/python3
"""
Module To Give Change
"""


def makeChange(coins, total):
    """
    Given a pile of coins of different values,
    determine the fewest number of coins needed to meet a given total total.
    """
    dp = [total + 1] * (total + 1)
    dp[0] = 0
    # Solve every subproblem from 1 to total
    for i in range(1, total + 1):
        # For each coin we are given
        for j in range(0, len(coins)):
            # If it is less than or equal to the sub problem total
            if coins[j] <= i:
                # Try it. See if it gives us a more optimal solution
                dp[i] = min(dp[i], dp[i - coins[j]] + 1)
    return -1 if dp[total] > total else dp[total]
