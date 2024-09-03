# class written with the help of the dataclass decorator

from dataclasses import dataclass

@dataclass(frozen=True)
class Coordinate:
    lat: float
    lon: float
    
    def __str__(self) -> str:
        ns = 'N' if self.lat >= 0 else 'S'
        we = 'E' if self.lon >= 0 else 'W'
        return f'{abs(self.lat):.1f}°{ns}, {abs(self.lon):.1f}°{we}'
    
moscow = Coordinate(55.76, 37.62)

location = Coordinate(55.76, 37.62)

assert moscow == location

assert (moscow.lat, moscow.lon) == (location.lat, location.lon)

assert str(moscow) == '55.8°N, 37.6°E'

# Coordinate is not a subclass of tuple, the decorator does not interfere with the use of inheritance
assert not issubclass(Coordinate, tuple)
    