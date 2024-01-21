#!/usr/bin/python3
def minOperations(number):
    res = 0
    i = 2
    pri = 1
    while i <= number:
        if number % i == 0:
            pri = i
            i += pri
            res += 2
        else:
            i += pri
            res += 1
    return res
