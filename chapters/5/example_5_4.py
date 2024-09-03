#  Defining and using a named tuple type

from collections import namedtuple

City = namedtuple("City", "name country population coordinates")

tokyo = City("Tokyo", "JP", 36.933, (35.689722, 139.691667))

assert (
    str(tokyo)
    == "City(name='Tokyo', country='JP', population=36.933, coordinates=(35.689722, 139.691667))"
)

# Accessing value by field name
assert tokyo.population == 36.933

# Accessing value by field position
assert tokyo[2] == 36.933