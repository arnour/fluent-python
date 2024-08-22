# Example of two-dimensional vector

import math


class Vector:

    def __init__(self, x: int = 0, y: int = 0) -> None:
        self.x: int = x
        self.y: int = y

    def __repr__(self) -> str:
        return f"Vector({self.x!r}, {self.y!r})"

    def __abs__(self) -> float:
        return math.hypot(self.x, self.y)

    def __bool__(self) -> bool:
        return bool(abs(self))

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, scalar) -> "Vector":
        return Vector(self.x * scalar, self.y * scalar)

    def __eq__(self, other: "Vector") -> bool:
        return self.x == other.x and self.y == other.y


# Adding two vectors
assert Vector(1, 2) + Vector(3, 4) == Vector(
    4, 6
), "Vector(1, 2) + Vector(3, 4) should result in Vector(4, 6)"

# Calculates the magnitude of a Vector
assert abs(Vector(3, 4)) == 5, "The magnnitude of the Vector(3, 4) should be 5"

# Scalar multiplication
assert Vector(3, 9) * 3 == Vector(
    9, 27
), "Vector(3, 9) * 3 should result in Vector(9, 27)"

# string representation
assert repr(Vector(3, 56)) == "Vector(3, 56)"

# string printing
assert (
    str(Vector(3, 56)) == "Vector(3, 56)"
), "String printing of Vector(3, 56) should be repr"

# Boolean value
assert not bool(Vector(0, 0)), "A vector with magnitude zero should be False"
