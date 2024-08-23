#!/usr/bin/python3
"""
Module To Give Change
"""


def makeChange(coins, total):
    """
    Given a pile of coins of different values,
    determine the fewest number of coins needed
    to meet a given amount total using
    a tree-based approach with memoization.
    Returns the fewest number of coins,
    or -1 if the total cannot be met by any combination of coins.
    """
    if total <= 0:
        return 0

    # Memoization dictionary to store already computed results
    memo = {}

    def helper(remaining):
        # Base case: no coins needed if remaining is 0
        if remaining == 0:
            return 0
        # Base case: no solution possible if remaining is negative
        if remaining < 0:
            return float("inf")
        # Check memoization dictionary to avoid redundant calculations
        if remaining in memo:
            return memo[remaining]

        # Initialize the minimum coins required to a large value
        min_coins = float("inf")

        # Explore all possible coin choices
        # (each coin corresponds to a branch in the tree)
        for coin in coins:
            result = helper(remaining - coin)
            if result != float("inf"):
                min_coins = min(min_coins, result + 1)

        # Store the result in the memoization dictionary
        memo[remaining] = min_coins
        return min_coins

    # Get the result for the total amount
    result = helper(total)
    return result if result != float("inf") else -1
