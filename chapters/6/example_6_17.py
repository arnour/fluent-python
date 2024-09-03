# A tuple built from another is actually the same exact tuple

t1 = (1, 2, 3)
t2 = tuple(t1)

assert t2 is t1

t3 = t1[:]

assert t3 is t1
