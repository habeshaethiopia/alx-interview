#!/usr/bin/python3
"""The pascal triangle enterview questions module"""


def pascal_triangle(n):
    """the function implimentation"""
    ans = []
    for i in range(n):
        temp = [1]
        if i == 1:
            temp = [1, 1]
        for j in range(i - 1):
            print(ans, j)
            temp.append(ans[-1][j] + ans[-1][j + 1])
        if len(ans) > 1:
            temp += [1]
        ans.append(temp)
    return ans
