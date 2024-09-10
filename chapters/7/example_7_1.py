#  Create and test a function, then read its __doc__ and check its type

def factorial(n) -> int:
    """returns n!"""
    return 1 if n < 2 else n * factorial(n - 1)

assert factorial(42) == 1405006117752879898543142606244511569936384000000000
assert factorial.__doc__ == 'returns n!'
assert str(type(factorial)) == "<class 'function'>"

