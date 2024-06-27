#!/usr/bin/python3
"""
Pascal triangle
"""


def generate_pattern(power):
    """
    Generate a row of Pascal's Triangle using binomial coefficients.

    Args:
    power (int): The row number of Pascal's Triangle to generate.

    Returns:
    list[int]: The generated row of Pascal's Triangle.
    """
    # Initialize an empty list to store the pattern
    pattern = []

    # Generate the pattern using binomial coefficients
    for i in range(power + 1):
        coefficient = binomial_coefficient(power, i)
        pattern.append(coefficient)
    return pattern


def binomial_coefficient(n, k):
    """
    Calculate binomial coefficient (n choose k) using an iterative approach.

    Args:
    n (int): The number of items.
    k (int): The number of items to choose.

    Returns:
    int: The binomial coefficient.
    """
    # Calculate the binomial coefficient "n choose k"
    if k == 0 or k == n:
        return 1
    return binomial_coefficient(n - 1, k - 1) + binomial_coefficient(n - 1, k)


def pascal_triangle(n):
    """
    Create Pascal's Triangle up to the nth row.

    Args:
    n (int): The number of rows of Pascal's Triangle to generate.

    Returns:
    list[list[int]]: The generated Pascal's Triangle.
    """
    pascal_triangle = []
    if n <= 0 or not:
        return []
    for i in range(n):
        pascal_triangle.append(generate_pattern(i))
    return pascal_triangle
