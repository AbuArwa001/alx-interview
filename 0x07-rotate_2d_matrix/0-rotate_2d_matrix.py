#!/usr/bin/python3
"""
Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """
    Rotate 2d matrix clockwise
    matrix = [
             [1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]
             ]
    """
    # row_size = len(matrix[0])
    # length = int(row_size / 2)

    # for i in range(length):
    #     for j in range(i, row_size - i - 1):
    #         # Save the top element
    #         temp = matrix[i][j]

    #         # Move left element to top
    #         matrix[i][j] = matrix[row_size - 1 - j][i]

    #         # Move bottom element to left
    #         matrix[row_size - 1 - j][i]
    #               = matrix[row_size - 1 - i][row_size - 1 - j]

    #         # Move right element to bottom
    #         matrix[row_size - 1 - i][row_size - 1 - j]
    #               = matrix[j][row_size - 1 - i]

    #         # Assign temp to right
    #         matrix[j][row_size - 1 - i] = temp
    # row_size = len(matrix[0])
    # length = row_size // 2

    # [
    #     matrix[i][j] if (temp := matrix[i][row_size-1-j],
    #                     matrix[i][row_size-1-j] := matrix[j][i],
    #                     matrix[j][i] := matrix[row_size-1-i][j],
    #                     matrix[row_size-1-i][j] :=
    #                       matrix[row_size-1-j][row_size-1-i],
    #                     matrix[row_size-1-j][row_size-1-i] :=
    #                               temp) is None else None
    #     for i in range(length)
    #     for j in range(i, row_size - i - 1)
    # ]

    row_size = len(matrix[0])
    length = int(row_size / 2)

    for i in range(length):
        j = i
        for j in range(i, row_size - i - 1):
            temp = matrix[i][row_size-j-1]
            matrix[i][row_size-1-j] = matrix[j][i]
            matrix[j][i] = matrix[row_size-1-i][j]
            matrix[row_size-1-i][j] = matrix[row_size-1-j][row_size-1-i]
            matrix[row_size-1-j][row_size-1-i] = temp
            j = j + 1
