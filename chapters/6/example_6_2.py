# Variables are bound to objects only after the objects are created


class Gizmo:
    def __init__(self) -> None:
        print(f"Gizmo id: {id(self)}")


x = Gizmo()

try:
    y = Gizmo() * 10
except TypeError as err:
    assert str(err) == "unsupported operand type(s) for *: 'Gizmo' and 'int'"
    
assert 'x' in dir()

# But variable y was never created, because the exception happened while the righthand side of the assignment was being evaluated
assert 'y' not in dir()
