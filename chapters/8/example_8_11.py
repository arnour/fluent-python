# Tuples as records

shangai: tuple[str, float, str] = ("Shangai", 24.38, "China")


PRECISION = 9


def encode(f1, f2, precision):
    pass


def geohash(lat_lon: tuple[float, float]) -> str:
    return encode(*lat_lon, PRECISION)
