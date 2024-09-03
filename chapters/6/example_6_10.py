# Cyclic references
from copy import deepcopy

a = [10, 20]

b = [a, 30]

a.append(b)

assert str(a) == "[10, 20, [[...], 30]]"

c = deepcopy(a)

assert str(c) == "[10, 20, [[...], 30]]"