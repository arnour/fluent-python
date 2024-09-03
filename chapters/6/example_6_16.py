# the end of an object’s life

import weakref

s1 = {1, 2, 3}

# s1 and s2 are aliases referring to the same set, {1, 2, 3}
s2 = s1


def bye():
    print("...object destroyed")


# Register the bye callback on the object referred by s1.
ender = weakref.finalize(s1, bye)

# The .alive attribute is True before the finalize object is called
assert ender.alive

#  del did not delete the object, just the s1 reference to it
del s1

assert ender.alive

# Rebinding the last reference, s2, makes {1, 2, 3} unreachable. It is destroyed, the bye callback is invoked, and ender.alive becomes False.
s2 = "spam"

assert not ender.alive
