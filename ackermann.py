# -*- coding: utf-8 -*-

def ackermann(m, n):
    if m == 0:
        return n + 1
    if n == 0:
        return ackermann(m - 1, 1)
    return ackermann(m - 1, ackermann(m, n - 1))


for m in range(0, 4):
    for n in range(0, 4):
        print("Ackermann({}, {}) = {}".format(m, n, ackermann(m, n)))
