#!/usr/bin/python3
"""script that reads stdin line by line
and computes metrics"""
import sys


# from collections import defaultdict
def my_print(dic: dict, size: int) -> None:
    """print the dictionary and the size"""
    print("File size: {}".format(size))
    for key, value in sorted(dic.items()):
        print("{}: {}".format(key, value))


def print_stats() -> None:
    """print stats"""
    size = 0
    c = 0
    dic = {}
    status = [200, 301, 400, 401, 403, 404, 405, 500]
    try:
        for s in sys.stdin:
            s = s.split()
            length = len(s)
            if length > 2:
                c += 1
                if c <= 10:
                    size += int(s[length - 1])
                    if int(s[-2]) in status:
                        dic[int(s[-2])] = (
                            1 if int(s[-2]) not in dic else dic[int(s[-2])] + 1
                        )
                    if c == 10:
                        my_print(dic, size)
                        c = 0

    finally:
        my_print(dic, size)


print_stats()
