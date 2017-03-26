#!/usr/bin/python

def gcf(a, b):
    while b%a > 0:
        a, b = min(a, b), max(a, b)
        b %= a
    return a


def pythagorean_triple(a):
    results = []
    for n in range(1, a):
        b_sq = 2*a*n + n**2
        if b_sq**.5 == int(b_sq**.5):
            b = int(b_sq**.5)
            if True or gcf(a, b) == 1:
                c = int((a**2 + b_sq) **.5)
                triple = [a, b, c]
                triple.sort()
                if not triple in results:
                    results.append(triple)

    return results

processed = []
for i in range(1, 500):
    triples = pythagorean_triple(i)
    if len(triples) > 0:
        for pt in triples:
            if not pt in processed:
                processed.append(pt)
                total = reduce(lambda x, y: x+y, pt)
#                if total > 950 and total < 1050:
                print pt, total
                if total == 1000:
                    print "Found target"
                    break
