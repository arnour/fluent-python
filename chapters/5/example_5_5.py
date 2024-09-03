# Named tuple attributes and methods

from collections import namedtuple
import json

Coordinate = namedtuple("Coordinate", "lat lon")

City = namedtuple("City", "name country population coordinates")

delhi_data = ("Delhi NCR", "IN", 21.935, (28.613889, 77.208889))

delhi = City._make(delhi_data)

assert delhi._asdict() == {
    "name": "Delhi NCR",
    "country": "IN",
    "population": 21.935,
    "coordinates": Coordinate(lat=28.613889, lon=77.208889),
}

assert json.dumps(delhi._asdict()) == """{"name": "Delhi NCR", "country": "IN", "population": 21.935, "coordinates": [28.613889, 77.208889]}"""