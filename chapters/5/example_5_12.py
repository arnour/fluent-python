# Inspecting a class decorated with dataclass

from dataclasses import dataclass


def assertCantSetAttributeError(f, msg):
    try:
        f()
        assert False, "It should have raised AttributeError"
    except AttributeError as err:
        assert str(err) == msg


@dataclass
class DemoDataClass:
    a: int
    b: float = 1.1
    c = "spam"


assert DemoDataClass.__annotations__ == {"a": int, "b": float}
assert DemoDataClass.__doc__ == "DemoDataClass(a: int, b: float = 1.1)"

assertCantSetAttributeError(
    lambda: DemoDataClass.a, "type object 'DemoDataClass' has no attribute 'a'"
)
assert DemoDataClass.b == 1.1
assert DemoDataClass.c == "spam"


d = DemoDataClass(9)

# Again, a and b are instance attributes, and c is a class attribute we get via the instance.
assert d.a == 9
assert d.b == 1.1
assert d.c == "spam"

# As mentioned, DemoDataClass instances are mutable—and no type checking is done at runtime
d.a = 10
d.b = "oops"
d.c = "whatever"
d.z = "secret"

assert d.a == 10
assert d.b == "oops"
assert d.c == "whatever"
assert d.z == "secret"
