#!/usr/bin/python

sqrt_5 = 5**.5
phi = (1 + sqrt_5) / 2
nphi = (1 - sqrt_5) / 2

def calc_fib(n):
    global phi, nphi, sqrt_5
    fib = int((phi**n - nphi**n) / sqrt_5)

    print n, fib
    return fib

total = 0
for i in range(0, 1001, 3):
    fib = calc_fib(i)
    if fib > 4000000:
        break
    total += fib

print "Total %s" % total
