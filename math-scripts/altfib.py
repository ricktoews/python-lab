def altfib(a, b):
    def fib(n):
        if n == 1:
            result = a
        elif n == 2:
            result = b
        else:
            result = fib(n-2) + fib(n-1)
        return result
    return fib

