#!/usr/bin/python3
"""module for interview question called lockbox"""


def canUnlockAll(rooms):
    """method that determines if all the boxes can be opened"""
    opened = set()
    queue = [0]
    while queue:
        x = queue.pop(0)
        if x not in opened:
            opened.add(x)
            queue.extend(rooms[x])
    return len(opened) == len(rooms)
