# Use factorial through a different name, and pass factorial as an argument


def factorial(n) -> int:
    """returns n!"""
    return 1 if n < 2 else n * factorial(n - 1)


fact = factorial

assert fact(5) == 120

assert list(map(fact, range(11))) == [
    1,
    1,
    2,
    6,
    24,
    120,
    720,
    5040,
    40320,
    362880,
    3628800,
]
