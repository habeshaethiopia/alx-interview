#!/usr/bin/python3
"""module for interview question called lockbox"""


def canUnlockAll(boxes):
    """method that determines if all the boxes can be opened"""
    n = len(boxes)
    seen_boxes = set([0])
    unseen_boxes = set(boxes[0]).difference(set([0]))
    while len(unseen_boxes) > 0:
        boxIdx = unseen_boxes.pop()
        if not boxIdx or boxIdx >= n or boxIdx < 0:
            continue
        if boxIdx not in seen_boxes:
            unseen_boxes = unseen_boxes.union(boxes[boxIdx])
            seen_boxes.add(boxIdx)
    return n == len(seen_boxes)
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
