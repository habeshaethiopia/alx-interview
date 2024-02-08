#!/usr/bin/python3
"""interview question n queens"""
import sys
from itertools import permutations
n = int(sys.argv[1])
print([
            ["." * i + "Q" + "." * (n - i - 1) for i in p]
            for p in permutations(range(n))
            if len(set(map(lambda z: z[0] - z[1], enumerate(p))))
            == len(set(map(lambda z: z[0] + z[1], enumerate(p))))
            == n
        ])
