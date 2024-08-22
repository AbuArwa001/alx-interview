#!/usr/bin/python3
"""
Module To Give Change
"""


def makeChange(coins, total):
    """
    Given a pile of coins of different values,
    determine the fewest number of coins needed
    to meet a given amount total using a recursive approach with memoization.
    Returns the fewest number of coins,
    or -1 if the total cannot be met by any combination of coins.
    """
    if total <= 0:
        return 0

    # Memoization dictionary to store already computed results
    memo = {}

    def helper(remainder):
        # If the remainder is 0, no more coins are needed
        if remainder == 0:
            return 0

        # If the remainder is less than 0, no solution is possible
        if remainder < 0:
            return float('inf')

        # If the result is already computed, return it
        if remainder in memo:
            return memo[remainder]

        # Initialize the minimum number of coins to a large value
        min_coins = float('inf')

        # Try every coin and choose the one that leads to the fewest coins
        for coin in coins:
            num_coins = helper(remainder - coin)
            if num_coins != float('inf'):
                min_coins = min(min_coins, num_coins + 1)

        # Store the computed result in the memo dictionary
        memo[remainder] = min_coins
        return min_coins

    # Call the helper function and handle the case where no solution exists
    result = helper(total)
    return result if result != float('inf') else -1
