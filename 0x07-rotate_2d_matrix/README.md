# 0x07. Rotate 2D Matrix

## Project Overview
The task for this project is to implement an in-place algorithm to rotate an `n x n` 2D matrix by 90 degrees clockwise. This project focuses on matrix manipulation and in-place operations, requiring a strong understanding of how to efficiently modify a matrix in Python without using additional space.

## Key Concepts

### Matrix Representation in Python
- **2D Matrices:** In Python, a 2D matrix can be represented as a list of lists. Each sublist represents a row in the matrix.
- **Accessing Elements:** You can access and modify elements using double indexing, e.g., `matrix[i][j]`.

### In-place Operations
- **In-place Modification:** Perform operations that directly modify the data structure without creating copies, minimizing space complexity.

### Matrix Transposition
- **Transposition:** This involves swapping rows and columns, an essential step in rotating the matrix.

### Reversing Rows
- **Row Reversal:** After transposing the matrix, reversing each row completes the 90-degree rotation.

### Nested Loops
- **Iterating through a Matrix:** Nested loops are essential for traversing and modifying 2D matrices.

## Resources

### Python Official Documentation
- [Data Structures](https://docs.python.org/3/tutorial/datastructures.html)
- [More on Lists](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)

### GeeksforGeeks Articles
- [Inplace rotate square matrix by 90 degrees](https://www.geeksforgeeks.org/inplace-rotate-square-matrix-by-90-degrees/)
- [Transpose a matrix in Single line in Python](https://www.geeksforgeeks.org/transpose-matrix-single-line-python/)

### TutorialsPoint
- [Python Lists](https://www.tutorialspoint.com/python/python_lists.htm)

## Approach
1. **Transpose the Matrix:** Convert rows into columns.
2. **Reverse Each Row:** After transposition, reverse each row to achieve the 90-degree rotation.

## Requirements
- **Editors:** vi, vim, emacs
- **Python Version:** 3.8.10
- **Style:** pycodestyle (version 2.8.0)
- **Modules:** No external modules allowed
- **Documentation:** All functions and modules must be documented
- **Executable Files:** Ensure all files are executable

## Task

### 0. Rotate 2D Matrix
- **Objective:** Given an `n x n` 2D matrix, rotate it 90 degrees clockwise.
- **Function Prototype:** `def rotate_2d_matrix(matrix):`
- **Constraints:**
  - Do not return anything. The matrix must be modified in-place.
  - Assume the matrix has 2 dimensions and is non-empty.

### Example
```python
#!/usr/bin/python3
"""
Test 0x07 - Rotate 2D Matrix
"""
rotate_2d_matrix = __import__('0-rotate_2d_matrix').rotate_2d_matrix

if __name__ == "__main__":
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

    rotate_2d_matrix(matrix)
    print(matrix)

# Output:
# [[7, 4, 1],
#  [8, 5, 2],
#  [9, 6, 3]]
