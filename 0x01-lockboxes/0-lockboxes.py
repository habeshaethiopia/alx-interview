#!/usr/bin/python3
"""module for interview question called lockbox"""


def canUnlockAll(rooms):
    """method that determines if all the boxes can be opened"""
    opened = set()
    queue = []
    while len(queue) > 0:
        x = queue.pop(0)
        if not x or x > len(rooms) or x < 0:
            continue
        if x not in opened:
            opened.add(x)
            queue.extend(rooms[x])
    return len(opened) == len(rooms)
