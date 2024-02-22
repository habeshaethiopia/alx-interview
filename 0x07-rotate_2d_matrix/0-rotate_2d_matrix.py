#!/usr/bin/python3
"""rotate image"""


def rotate_2d_matrix(matrix):
    """rotate image"""
    top = len(matrix) - 1
    bottom = 0
    while top > bottom:
        matrix[top], matrix[bottom] = matrix[bottom], matrix[top]
        top -= 1
        bottom += 1
    for i in range(len(matrix)):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
