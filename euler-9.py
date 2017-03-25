#!/usr/bin/python

def gcf(a, b):
    count = 0
    while count < 10:
        a, b = min(a, b), max(a, b)
        if b%a == 0:
            break
        b %= a
        count += 1

    return a


def pythagorean_triple(a):
    results = []
    for n in range(1, a):
        b_sq = 2*a*n + n**2
        if b_sq**.5 == int(b_sq**.5):
            b = int(b_sq**.5)
            if True or gcf(a, b) == 1:
                c = int((a**2 + b_sq) **.5)
                results = [b, a, c]

    return results

for i in range(3, 5000):
    pt = pythagorean_triple(i)
    if len(pt) > 0:
        total = reduce(lambda x, y: x+y, pt)
        print pt, total
        if total == 1000:
            print "Found target"
            break
