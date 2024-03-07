#!/usr/bin/python3
"""the perimeter of the island"""


def island_perimeter(grid):
    """the perimeter of the island"""
    p = 0
    L = len(grid)
    W = len(grid[0])
    for i, a in enumerate(grid):
        for j, b in enumerate(a):
            if b == 1:
                if i == 0 or grid[i - 1][j] == 0:
                    p = p + 1
                if j == 0 or grid[i][j - 1] == 0:
                    p = p + 1
                if i == L - 1 or grid[i + 1][j] == 0:
                    p = p + 1
                if j == W - 1 or grid[i][j + 1] == 0:
                    p = p + 1
    return p
