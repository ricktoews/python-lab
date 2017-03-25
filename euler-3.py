#!/usr/bin/python
import sys

safety = 0
def first_factor(n):
    global safety
    safety += 1
    if safety > 100:
        return

    max = int(n**.5)
    first = n
    f = 3
    while f <= max:
        if n % f == 0:
            first = f
            break
        f += 2

    print first
    if first == n:
        return first
    else:
        return first_factor(n / first)

arg = int(sys.argv[1])
first_factor(arg)
