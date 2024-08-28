# 0x09. Island Perimeter

This project focuses on calculating the perimeter of an island described in a grid (2D list). The grid is composed of integers where `0` represents water and `1` represents land. The island is surrounded by water, and there is only one island with no lakes (water within the island).

## Concepts and Skills Needed

### 1. 2D Arrays (Matrices)
- **Access and Iteration:** Learn how to navigate through a 2D array, accessing and iterating over each element.
- **Adjacent Cells:** Understand how to move horizontally and vertically within the grid to identify neighboring cells.

### 2. Conditional Logic
- **Edge Calculation:** Apply logical conditions to determine when a cell is part of the perimeter.
- **Cell Contribution:** Identify conditions under which a land cell's edges contribute to the island's perimeter.

### 3. Counting Techniques
- **Perimeter Counting:** Develop a method to count the edges that contribute to the perimeter based on the conditions.

### 4. Problem-Solving Strategies
- **Task Breakdown:** Approach the problem by breaking it down into smaller, manageable tasks such as identifying land cells and calculating their contribution to the perimeter.

### 5. Python Programming
- **Nested Loops:** Use nested loops to iterate through each cell in the grid.
- **Conditional Statements:** Implement conditions to check the status of adjacent cells and calculate the perimeter.

## Resources

### Python Official Documentation
- **Nested Lists:** Learn how to work with lists within lists in Python.

### GeeksforGeeks Articles
- **Python Multi-dimensional Arrays:** A guide to working with 2D arrays in Python effectively.

### TutorialsPoint
- **Python Lists:** A comprehensive guide on creating, accessing, and manipulating lists in Python, essential for working with grids.

### YouTube Tutorials
- **Python 2D Arrays and Lists:** Visual tutorials to reinforce your understanding of 2D arrays and lists in Python.

## Additional Resources
- **Mock Technical Interviews:** Practice problem-solving techniques in a technical interview setting.

## Requirements

- **General:**
  - Allowed editors: `vi`, `vim`, `emacs`
  - Files will be interpreted/compiled on Ubuntu 20.04 LTS using Python 3 (version 3.4.3)
  - All files should end with a new line
  - The first line of all files should be exactly `#!/usr/bin/python3`
  - A `README.md` file at the root of the folder is mandatory
  - Code must adhere to PEP 8 style (version 1.7)
  - No external modules are allowed to be imported
  - All modules and functions must be documented
  - All files must be executable

## Tasks

### 0. Island Perimeter
- **Mandatory Task:** Create a function `def island_perimeter(grid):` that returns the perimeter of the island described in the grid.
- **Details:**
  - `grid` is a list of list of integers:
    - `0` represents water
    - `1` represents land
  - Each cell is square, with a side length of 1
  - Cells are connected horizontally/vertically (not diagonally)
  - `grid` is rectangular, with its width and height not exceeding 100
  - The grid is completely surrounded by water
  - There is only one island (or none)
  - The island doesn’t have “lakes” (water inside that isn’t connected to the water surrounding the island)

### Example

```python
#!/usr/bin/python3
"""
0-main
"""
island_perimeter = __import__('0-island_perimeter').island_perimeter

if __name__ == "__main__":
    grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    print(island_perimeter(grid))  # Output should be 12
