#! /usr/bin/python

total = 0

def isBy5(total):
    for i in range(5, 1000, 5):
        if i % 3 > 0:
            total += i

    return total

def isBy3(total):
    for i in range(3, 1000, 3):
        total += i

    return total

total = isBy5(total)
total = isBy3(total)
print total
