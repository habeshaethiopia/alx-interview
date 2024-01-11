#!/usr/bin/python3
"""module for interview question called lockbox"""


def canUnlockAll(rooms):
    """method that determines if all the boxes can be opened"""
    opened = set()
    stack = [0]
    while len(stack) > 0:
        x = stack.pop()
        if x not in opened:
            opened.add(x)
            stack.extend(rooms[x])
    else:
        return set(range(len(rooms))).issubset(set(opened))
