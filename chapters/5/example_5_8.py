from typing import NamedTuple

class Coordinate(NamedTuple):
    lat: float
    lon: float
    reference: str = 'WGS84'
    
coordinate = Coordinate(0, 0)

assert coordinate.reference == "WGS84"

assert Coordinate._field_defaults == {"reference": "WGS84"}