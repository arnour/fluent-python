# Demo of attrgetter to process a previously defined list of namedtuple called metro_data

from collections import namedtuple

LatLon = namedtuple("LatLon", "lat lon")

Metropolis = namedtuple("Metropolis", "name cc pop coord")

metro_data = [
    ("Tokyo", "JP", 36.933, (35.689722, 139.691667)),
    ("Delhi NCR", "IN", 21.935, (28.613889, 77.208889)),
    ("Mexico City", "MX", 20.142, (19.433333, -99.133333)),
    ("New York-Newark", "US", 20.104, (40.808611, -74.020386)),
    ("São Paulo", "BR", 19.649, (-23.547778, -46.635833)),
]

metro_areas = [
    Metropolis(name, cc, pop, LatLon(*coord)) for name, cc, pop, coord in metro_data
]


tokyo = metro_areas[0]

assert tokyo == Metropolis("Tokyo", "JP", 36.933, LatLon(35.689722, 139.691667))
assert tokyo.coord.lat == 35.689722

from operator import attrgetter

# Define an attrgetter to retrieve the name and the coord.lat nested attribute
name_lat = attrgetter("name", "coord.lat")

assert tuple([name_lat(metropolis) for metropolis in metro_areas]) == (
    ("Tokyo", 35.689722),
    ("Delhi NCR", 28.613889),
    ("Mexico City", 19.433333),
    ("New York-Newark", 40.808611),
    ("São Paulo", -23.547778),
)
