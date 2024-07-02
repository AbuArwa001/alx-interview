# Box Unlocking Algorithm

This project contains a Python implementation of an algorithm to determine if all boxes can be unlocked starting from the first box. Each box may contain keys to other boxes, and the goal is to use these keys to open all boxes.

## Functions

### `append_lst_ls(my_list, element_to_add)`

Appends elements from `element_to_add` to `my_list` if they are not already in `my_list` and are not zero.

**Parameters:**
- `my_list` (list): The list to which elements will be added.
- `element_to_add` (list): The list of elements to add to `my_list`.

**Returns:**
- `list`: The updated `my_list` with elements added from `element_to_add`.

### `canUnlockAll(boxes)`

Determines if all boxes can be unlocked starting from the first box.

**Parameters:**
- `boxes` (list of lists): A list where each element is a list of keys contained in that box.

**Returns:**
- `bool`: `True` if all boxes can be unlocked, `False` otherwise.

## Usage

To use these functions, simply import them into your Python script and call them with the appropriate parameters.

Example:

```python
from box_unlocking import append_lst_ls, canUnlockAll

# Define the boxes with keys
boxes = [[1, 2], [3, 4], [2], [], [0]]

# Check if all boxes can be unlocked
result = canUnlockAll(boxes)

print(result)  # Output will be True or False based on the input
