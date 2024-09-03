# Named tuple attributes and methods
from collections import namedtuple


Coordinate = namedtuple("Coordinate", "lat lon reference", defaults=["WGS84"])

coordinate = Coordinate(0, 0)

assert coordinate.reference == "WGS84"

assert Coordinate._field_defaults == {"reference": "WGS84"}
