#  Using partial to use a two-argument function where a one-argument callable is required

from operator import mul
from functools import partial

# Create new triple function from mul, binding the first positional argument to 3
triple = partial(mul, 3)

assert triple(7) == 21

assert [triple(i) for i in range(1, 10)] == [3, 6, 9, 12, 15, 18, 21, 24, 27]
