#

import typing


def assertCantSetAttributeError(f, msg):
    try:
        f()
        assert False, "It should have raised AttributeError"
    except AttributeError as err:
        assert str(err) == msg


class DemoNTClass(typing.NamedTuple):
    a: int
    b: float = 1.1
    c = "spam"


assert DemoNTClass.__annotations__ == {"a": int, "b": float}

# The a and b class attributes are descriptors

print(DemoNTClass.a)
print(DemoNTClass.b)
print(DemoNTClass.c)

assert DemoNTClass.c == "spam"

assert DemoNTClass.__doc__ == "DemoNTClass(a, b)"

nt = DemoNTClass(8)

assert nt.a == 8

assert nt.b == 1.1

assert nt.c == "spam"


def setA() -> None:
    nt.a = 99


def setB() -> None:
    nt.b = 99.99


def setC() -> None:
    nt.c = "xx"


# If you try to assign values to nt.a, nt.b, nt.c, or even nt.z,
# you’ll get Attribute Error exceptions with subtly different error messages.
assertCantSetAttributeError(setA, "can't set attribute")

assertCantSetAttributeError(setB, "can't set attribute")

assertCantSetAttributeError(setC, "'DemoNTClass' object attribute 'c' is read-only")
