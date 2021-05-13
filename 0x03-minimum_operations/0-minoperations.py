#!/usr/bin/python3
"""Finds the minimun operations needed to have a given amount of H characters
"""

from math import sqrt


def minOperations(n):
    min_ops = 0

    if n <= 1:
        return 0

    for i in range(2, int(sqrt(n) + 1)):
        while n % i == 0:
            min_ops += i
            n = n / i
            if n <= 1:
                break

    min_ops += int(n)

    return min_ops
