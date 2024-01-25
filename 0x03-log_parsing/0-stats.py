#!/usr/bin/python3
"""script that reads stdin line by line
and computes metrics"""
import sys

# from collections import defaultdict
size = 0
c = 0
dic = {}
while True:
    try:
        s = input().split()

        dic[int(s[-2])] = 1 if int(s[-2]) not in dic else dic[int(s[-2])] + 1
        l = len(s)

        size += int(s[l - 1])
        if c % 10 == 0:
            if dic:
                for key, value in sorted(dic.items()):
                    print("{}: {}".format(key, value))
            print("File size: {}".format(size))
            dic.clear()
        c += 1
    except KeyboardInterrupt:
        print("File size: {}".format(size))
