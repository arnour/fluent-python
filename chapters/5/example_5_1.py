class Coordinate:
    def __init__(self, lat, lon) -> None:
        self.lat = lat
        self.lon = lon

moscow = Coordinate(55.76, 37.62)

location = Coordinate(55.76, 37.62)

assert moscow != location

assert (moscow.lat, moscow.lon) == (location.lat, location.lon)

