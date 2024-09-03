from typing import NamedTuple

class Coordinate(NamedTuple):
    lat: float
    lon: float
    reference: str = 'WGS84'
    
coordinate = Coordinate('Ni!', None)

assert coordinate == ('Ni!', None, 'WGS84')

# run mypy example_5_9.py