#  Lists of factorials produced with map and filter compared to alternatives coded as list comprehensions


def factorial(n) -> int:
    """returns n!"""
    return 1 if n < 2 else n * factorial(n - 1)


assert list(map(factorial, range(6))) == [1, 1, 2, 6, 24, 120]
assert [factorial(i) for i in range(6)] == [1, 1, 2, 6, 24, 120]

# List comprehension does the same job, replacing map and filter, and making lambda unnecessary
assert list(map(factorial, filter(lambda n: n % 2, range(6)))) == [1, 6, 120]
assert [factorial(i) for i in range(6) if i % 2] == [1, 6, 120]
