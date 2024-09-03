from typing import NamedTuple


class Coordinate(NamedTuple):
    lat: float
    lon: float

    def __str__(self):
        ns = 'N' if self.lat >= 0 else 'S'
        we = 'E' if self.lon >= 0 else 'W'
        return f'{abs(self.lat):.1f}°{ns}, {abs(self.lon):.1f}°{we}'    
moscow = Coordinate(55.76, 37.62)

location = Coordinate(55.76, 37.62)

assert moscow == location

assert (moscow.lat, moscow.lon) == (location.lat, location.lon)

assert str(moscow) == '55.8°N, 37.6°E'

# Coordinate is not a subclass of NamedTuple, since NamedTuple uses the functionality of metaclass to create a tuple-like object
assert issubclass(Coordinate, tuple)
