#!/usr/bin/python3
"""script that reads stdin line by line
and computes metrics"""
import sys

# from collections import defaultdict
def print_stats()-> None:
    """print stats"""
    
    size = 0
    c = 0
    dic = {}
    status = [200, 301, 400, 401, 403, 404, 405, 500]
    while True:
        try:
            s = input().split()
            length = len(s)
            size += int(s[length - 1])
            if c % 10 == 0:
                if dic:
                    for key, value in sorted(dic.items()):
                        print("{}: {}".format(key, value))
                print("File size: {}".format(size))
                dic.clear()
            if int(s[-2]) in status:
                dic[int(s[-2])] = 1 if int(s[-2]) not in dic else dic[int(s[-2])] + 1

            c += 1
        except KeyboardInterrupt:
            print("File size: {}".format(size))
if __name__ == "__main__":
    print_stats()