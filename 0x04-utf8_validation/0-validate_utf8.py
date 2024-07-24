#!/usr/bin/python3
"""
Module containing validUTF8 and isUtf8  function
file for testing
"""


def validUTF8(data):
    """
    Determine if a given data set represents a valid UTF-8 encoding.

    Args:
        data (List[int]): The list of integers to validate.

    Returns:
        bool: True if data is a valid UTF-8 encoding, else False.
    """
    def is_valid_byte(byte, mask, bits_to_match):
        return byte & mask == bits_to_match

    n_bytes = 0
    if len(data) == 1 and data[0] >> 7 == 0:
        return True
    for num in data:
        if n_bytes == 0:
            if num >> 5 == 0b110:
                n_bytes = 1
            elif num >> 4 == 0b1110:
                n_bytes = 2
            elif num >> 3 == 0b11110:
                n_bytes = 3
            elif num >> 7:
                return False
        else:
            if not is_valid_byte(num, 0b11000000, 0b10000000):
                return False
            n_bytes -= 1

    return n_bytes == 0
