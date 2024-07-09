#!/usr/bin/python3
"""
Module for calculating the minimum number
of operations to reach exactly n 'H' characters
in a text file using only 'Copy All' and 'Paste' operations.

This module contains the following functions:
- minOperations: Calculates the minimum number of operations needed.

Example Usage:
    if __name__ == "__main__":
        print(minOperations(1))
        # Output: 0
        print(minOperations(4))
        # Output: 4 (Copy all, Paste, Paste)
        print(minOperations(9))
        # Output: 6 (Copy all, Paste, Paste, Paste, Paste, Paste)
        print(minOperations(15))
        # Output: 8 (Copy all, Paste, Paste, Copy all, Paste, Paste, Paste)
"""


def minOperations(n: int) -> int:
    """
    Calculate the minimum number of operations
    needed to reach exactly n H characters
    in a text file, starting with a single 'H'.
    You can only use two operations:
    Copy All and Paste.

    Args:
        n (int): The target number of 'H' characters.

    Returns:
        int: The minimum number of operations required.
    """
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations
