# Tuples as records with named fields

from typing import NamedTuple


class Coordinate(NamedTuple):
    lat: float
    lon: float


PRECISION = 9


def encode(f1, f2, precision):
    pass


def geohash(lat_lon: tuple[float, float]) -> str:
    return encode(*lat_lon, PRECISION)


def display(lat_lon: tuple[float, float]) -> str:
    lat, lon = lat_lon
    ns = "N" if lat >= 0 else "S"
    ew = "E" if lon >= 0 else "W"
    return f"{abs(lat):0.1f}°{ns}, {abs(lon):0.1f}°{ew}"


geohash(Coordinate(1, 2))
assert display(Coordinate(1, 2)) == "1.0°N, 2.0°E"
