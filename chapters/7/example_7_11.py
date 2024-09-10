# Packages for Functional Programming
from functools import reduce
from operator import mul

def factorial(n):
    return reduce(lambda a, b: a * b, range(1, n + 1))

def factorial2(n):
    return reduce(mul, range(1, n + 1))


assert factorial(4) == 24
assert factorial2(4) == 24