# Tuples used as records

from typing import Tuple, List

lax_coordinates: Tuple[float, float] = (33.9425, -118.408056)
city, year, pop, chg, area = ("Tokyo", 2003, 32_450, 0.66, 8014)
traveler_ids: List[Tuple[str, str]] = [
    ("USA", "31195855"),
    ("BRA", "CE342567"),
    ("ESP", "XDA205856"),
]

# As we iterate over the list, passport is bound to each tuple
# The % formatting operator understands tuples and treats each item as a separate field.
for passaport in sorted(traveler_ids):
    print("%s/%s" % passaport)

# The for loop knows how to retrieve the items of a tuple separately—this is called “unpacking.”
# Here we are not interested in the second item, so we assign it to _, a dummy variable.
for country, _ in traveler_ids:
    print(country)
