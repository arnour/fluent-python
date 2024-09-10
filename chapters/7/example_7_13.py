# Demo of itemgetter to sort a list of tuples
from operator import itemgetter

metro_data = [
    ("Tokyo", "JP", 36.933, (35.689722, 139.691667)),
    ("Delhi NCR", "IN", 21.935, (28.613889, 77.208889)),
    ("Mexico City", "MX", 20.142, (19.433333, -99.133333)),
    ("New York-Newark", "US", 20.104, (40.808611, -74.020386)),
    ("São Paulo", "BR", 19.649, (-23.547778, -46.635833)),
]

#  itemgetter(1) creates a function that, given a collection, returns the item at index 1
sorted_metro_data = sorted(metro_data, key=itemgetter(1))

assert sorted_metro_data[0] == ("São Paulo", "BR", 19.649, (-23.547778, -46.635833))

# If you pass multiple index arguments to itemgetter,
# the function it builds will return tuples with the extracted values,
# which is useful for sorting on multiple keys
cc_name = itemgetter(1, 0)

assert tuple(cc_name(city) for city in metro_data) == (
    ("JP", "Tokyo"),
    ("IN", "Delhi NCR"),
    ("MX", "Mexico City"),
    ("US", "New York-Newark"),
    ("BR", "São Paulo"),
)
