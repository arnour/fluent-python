# The Meaning of Variable Annotations

def assertAttributeError(f, msg):
    try:
        f()
        assert False, 'It should have raised an Attribute error'
    except AttributeError as err:
        assert str(err) == msg

class DemoPlainClass:
    # a becomes an entry in __annotations__, but is otherwise discarded: no attribute named a is created in the class.
    a: int

    # b is saved as an annotation, and also becomes a class attribute with value 1.1
    b: float = 1.1

    # c is just a plain old class attribute, not an annotation.
    c = "spam"


assert DemoPlainClass.__annotations__ == {"a": int, "b": float}

# The a survives only as an annotation. It doesn’t become a class attribute because no value is bound to it.
assertAttributeError(lambda : DemoPlainClass.a, "type object 'DemoPlainClass' has no attribute 'a'")

# The b and c are stored as class attributes because they are bound to values.

assert DemoPlainClass.b == 1.1

assert DemoPlainClass.c == "spam"

# None of those three attributes will be in a new instance of DemoPlainClass

o = DemoPlainClass()

assertAttributeError(lambda : o.a, "'DemoPlainClass' object has no attribute 'a'")

# while o.b and o.c will retrieve the class attributes with values 1.1 and 'spam'—that’s just normal Python object behavior
assert o.b == DemoPlainClass.b

assert o.c == DemoPlainClass.c