# The unexpected result: item t2 is changed and an exception is raised

t = (1, 2, [30, 40])

try:
    t[2] += [50, 60]
except TypeError as err:
    # TypeError is raised with the message 'tuple' object does not support item assignment
    assert str(err) == "'tuple' object does not support item assignment"

# t becomes (1, 2, [30, 40, 50, 60]).
assert t == (1, 2, [30, 40, 50, 60])
