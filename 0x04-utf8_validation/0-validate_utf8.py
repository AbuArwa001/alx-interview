#!/usr/bin/python3
"""
Module containing validUTF8 and isUtf8  function
file for testing
"""
import math

def isUtf8(i: int) -> bool:
    """
    Function checking if the number has only 8 least significant bits
    containing validateUTF* function
    file for testing
    """
    count = 0
    for _ in range(32):
        i = math.floor(i/2)
        # print(i)
        count += 1
        if i < 1:
            break
    # print(count)
    return count <= 8
def validUTF8(data):
    """
    Function Return true if a list has all utf8 chars
    """
    for i in data:
        if isUtf8(i):
            continue
        else:
            return False
    return True