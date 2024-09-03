# The Relative Immutability of Tuples
# t1 and t2 initially compare equal, but changing a mutable item inside tuple t1 makes it different

t1 = (1, 2, [30, 40])
t2 = (1, 2, [30, 40])

# they have the same content - Although distinct objects, t1 and t2 compare equal, as expected.
assert t1 == t2

t1_last_item_id = id(t1[-1])

# t1 is immutable, but t1[-1] is mutable
t1[-1].append(99)

# The identity of t1[-1] has not changed, only its value
assert t1_last_item_id == id(t1[-1])

assert t1 == (1, 2, [30, 40, 99])

# t1 and t2 are now different
assert t1 != t2