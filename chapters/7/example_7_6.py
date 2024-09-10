# Sum of integers up to 99 performed with reduce and sum

from functools import reduce
from operator import add

# Same task with sum—no need to import and call reduce and add
assert reduce(add, range(100)) == 4950
assert sum(range(100)) == 4950
