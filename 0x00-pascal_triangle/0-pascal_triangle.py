#!/usr/bin/python3
"""
Pascal triangle
"""


def pascal_triangle(n: int) -> list[list[int]]:
    """
    Create Pascal's Triangle up to the nth row.

    Args:
    n (int): The number of rows of Pascal's Triangle to generate.

    Returns:
    list[list[int]]: The generated Pascal's Triangle.
    """
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        triangle.append(generate_pattern(i))

    return triangle


def generate_pattern(power: int) -> list[int]:
    """
    Generate a row of Pascal's Triangle using binomial coefficients.

    Args:
    power (int): The row number of Pascal's Triangle to generate.

    Returns:
    list[int]: The generated row of Pascal's Triangle.
    """
    pattern = []
    for i in range(power + 1):
        coefficient = binomial_coefficient(power, i)
        pattern.append(coefficient)
    return pattern


def binomial_coefficient(n: int, k: int) -> int:
    """
    Calculate binomial coefficient (n choose k) using an iterative approach.

    Args:
    n (int): The number of items.
    k (int): The number of items to choose.

    Returns:
    int: The binomial coefficient.
    """
    if k > n - k:  # Take advantage of symmetry
        k = n - k
    c = 1
    for i in range(k):
        c = c * (n - i) // (i + 1)
    return c
