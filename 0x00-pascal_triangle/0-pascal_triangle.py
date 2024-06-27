#!/usr/bin/python3
"""
Pascal triangle
"""


def generate_pattern(power):
    # Initialize an empty list to store the pattern
    pattern = []

    # Generate the pattern using binomial coefficients
    for i in range(power + 1):
        coefficient = binomial_coefficient(power, i)
        pattern.append(coefficient)
    return pattern


def binomial_coefficient(n, k):
    # Calculate the binomial coefficient "n choose k"
    if k == 0 or k == n:
        return 1
    return binomial_coefficient(n - 1, k - 1) + binomial_coefficient(n - 1, k)

    return pattern


def pascal_triangle(n):
    pascal_triangle = []
    if n <= 0:
        return
    for i in range(n):
        pascal_triangle.append(generate_pattern(i))
    return pascal_triangle
