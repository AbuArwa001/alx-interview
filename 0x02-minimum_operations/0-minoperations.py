#!/usr/bin/python3
"""
Module for calculating the minimum number
of operations to reach exactly n 'H' characters
in a text file using only 'Copy All' and 'Paste' operations.

This module contains the following functions:
- isOdd: Checks if a number is odd.
- isPrime: Checks if a number is prime.
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


def isOdd(num: int) -> bool:
    """
    Check if a number is odd.

    Args:
        num (int): The number to check.

    Returns:
        bool: True if the number is odd, False otherwise.
    """
    return num % 2 != 0


def isPrime(num: int) -> bool:
    """
    Check if a number is prime.

    Args:
        num (int): The number to check.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


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
    copy_all = 1
    paste = 0
    h_chars = 1

    if n <= 1:
        return 0
    if isPrime(n):
        return n

    if isOdd(n):
        prev_copy = 1
        while h_chars != n:
            if h_chars * 3 == n:
                prev_copy = h_chars
                copy_all += 1
                h_chars *= 2
            else:
                h_chars += prev_copy
            paste += 1
        return copy_all + paste
    else:
        prev_copy = 1
        while h_chars != n:
            if h_chars == int(n / 2):
                prev_copy = h_chars
                copy_all += 1
                h_chars *= 2
            elif not isOdd(h_chars) and h_chars < (n / 4):
                prev_copy = h_chars
                h_chars *= 2
                copy_all += 1
            else:
                h_chars += prev_copy
            paste += 1
        return copy_all + paste
