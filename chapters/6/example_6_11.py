# A function may change any mutable object it receives


def f(a, b):
    a += b
    return a


x = 1
y = 2

assert (x, y) == (1, 2)

assert f(x, y) == 3

# The number x is unchanged.
assert (x, y) == (1, 2)

a = [1, 2]
b = [3, 4]

assert (a, b) == ([1, 2], [3, 4])

assert f(a, b) == [1, 2, 3, 4]

# The list a is changed.
assert (a, b) == ([1, 2, 3, 4], [3, 4])

t = (10, 20)
u = (30, 40)

assert (t, u) == ((10, 20), (30, 40))

assert f(t, u) == (10, 20, 30, 40)

# The tuple t is unchanged.
assert (t, u) == ((10, 20), (30, 40))