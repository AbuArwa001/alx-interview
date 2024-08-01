# 0x05. N Queens

## Project Overview
The N Queens problem is a classic challenge in computer science that involves placing N non-attacking queens on an N×N chessboard. This project will require you to use the backtracking algorithm to find all possible solutions for a given N.

## Objectives
- Implement a Python program that solves the N Queens problem using a backtracking algorithm.
- Your solution should be executable and adhere to PEP 8 style guidelines.
- The program must handle command-line arguments and provide appropriate error messages.

## Concepts to Master
1. **Backtracking Algorithms**
   - Learn how to use backtracking to explore and backtrack on potential solutions.
   - Reference: [Backtracking Introduction](https://en.wikipedia.org/wiki/Backtracking)

2. **Recursion**
   - Implement recursive functions to solve the problem using backtracking.
   - Reference: [Recursion in Python](https://realpython.com/python-recursion/)

3. **List Manipulations in Python**
   - Create and manipulate lists to represent the board and store solutions.
   - Reference: [Python Lists](https://docs.python.org/3/tutorial/introduction.html#lists)

4. **Python Command Line Arguments**
   - Handle command-line arguments using the `sys` module.
   - Reference: [Command Line Arguments in Python](https://docs.python.org/3/library/sys.html#sys.argv)

## Tasks
1. **N Queens**
   - Write a program that solves the N Queens problem.
   - **Usage:** `nqueens N`
     - If the program is called with an incorrect number of arguments, print `Usage: nqueens N` and exit with status 1.
     - If N is not an integer, print `N must be a number` and exit with status 1.
     - If N is less than 4, print `N must be at least 4` and exit with status 1.
   - The program should print each solution to the N Queens problem, one per line. Each solution is a list of lists where each inner list represents the position of a queen on the board.

## Example Output
```bash
$ ./0-nqueens.py 4
[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]

$ ./0-nqueens.py 6
[[0, 1], [1, 3], [2, 5], [3, 0], [4, 2], [5, 4]]
[[0, 2], [1, 5], [2, 1], [3, 4], [4, 0], [5, 3]]
[[0, 3], [1, 0], [2, 4], [3, 1], [4, 5], [5, 2]]
[[0, 4], [1, 2], [2, 0], [3, 5], [4, 3], [5, 1]]
