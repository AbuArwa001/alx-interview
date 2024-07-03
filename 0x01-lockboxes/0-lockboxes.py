#!/usr/bin/python3
"""
Module will Check if all boxes can be opened
"""


def append_lst_ls(my_list, element_to_add):
    """
    Appends elements from element_to_add to my_list
    if they are not already in my_list and are not zero.

    Args:
    my_list (list): The list to which elements will be added.
    element_to_add (list): The list of elements to add to my_list.

    Returns:
    list: The updated my_list with elements added from element_to_add.
    """
    for i in element_to_add:
        if i not in my_list and i != 0:
            my_list.append(i)
    return my_list


def canUnlockAll(boxes):
    """
    Determines if all boxes can be unlocked starting from the first box.

    Args:
    boxes (list of lists): A list where each element
    is a list of keys contained in that box.

    Returns:
    bool: True if all boxes can be unlocked, False otherwise.

    Raises:
    TypeError: If boxes is not a list of lists.
    """
    if not isinstance(boxes, list) or not all(
        isinstance(box, list) for box in boxes
    ):
        raise TypeError("boxes must be a list of lists")

    keys = [0]  # Start with the key to the first box (0)
    opened = [False] * len(boxes)  # Track which boxes have been opened
    opened[0] = True  # The first box is open
    keys = append_lst_ls(keys, boxes[0])  # Add keys from the first box

    for key in keys:
        if (
            key < len(boxes) and not opened[key]
        ):  # Only try to open unopened boxes within bounds
            opened[key] = True  # Mark the box as opened
            # Add keys from the newly opened box
            keys = append_lst_ls(keys, boxes[key])

    # Check if all boxes are opened
    return all(opened)
