#!/usr/bin/python3
"""UTF-8 Validation"""
from typing import List


def validUTF8(data: List[int]) -> bool:
    """from leetcode"""
    n = len(data)
    i = 0

    while i < n:
        valid_encoding = False
        if one_byte_encoding(data[i]):
            i += 1
            valid_encoding = True

        for byte_len in range(2, 4 + 1):
            if byte_encoding(byte_len, data, i):
                i += byte_len
                valid_encoding = True
                break

        if not valid_encoding:
            return False
    return True


def one_byte_encoding(number: int) -> bool:
    # check if 8th bit is set
    if number & 1 << 7 == 0:
        return True
    return False


def byte_encoding(byte_len, data, i) -> bool:
    # out of bound check
    if i + byte_len > len(data):
        return False

    # first byte should be byte_len 1's followed by 0
    first_byte = data[i]
    for j in range(byte_len):
        if first_byte & 1 << (7 - j) == 0:
            return False

    # check n+1 bit to be 0
    if first_byte & 1 << 7 - byte_len != 0:
        return False

    # the rest n-1 bytes should be 10xxxxxx
    for j in range(i + 1, i + 1 + (byte_len - 1)):
        # check 10xxxxxx
        if data[j] & 1 << 7 == 0:
            return False
        if data[j] & 1 << 6 != 0:
            return False
    return True


if __name__ == "__main__":
    data = [197, 130, 1]
    print(validUTF8(data))

    data = [235, 140, 4]
    print(validUTF8(data))

    data = [65]
    print(validUTF8(data))

    data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
    print(validUTF8(data))

    data = [229, 65, 127, 256]
    print(validUTF8(data))
