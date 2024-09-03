import typing


class City(typing.NamedTuple):
    continent: str
    name: str
    country: str


cities = [
    City("Asia", "Tokyo", "JP"),
    City("Asia", "Delhi", "IN"),
    City("North America", "Mexico City", "MX"),
    City("North America", "New York", "US"),
    City("South America", "São Paulo", "BR"),
]


def match_asian_cities():
    results = []
    for city in cities:
        match city:
            case City(continent="Asia"):
                results.append(cities)
    return results


def match_asian_cities_pos():
    results = []
    for city in cities:
        match city:
            case City("Asia"):
                results.append(cities)
    return results


def match_asian_countries():
    results = []
    for city in cities:
        match city:
            case City(continent="Asia", country=cc):
                results.append(cc)
    return results


def match_asian_countries_pos():
    results = []
    for city in cities:
        match city:
            case City("Asia", _, country):
                results.append(country)
    return results


assert len(match_asian_cities()) == 2

assert match_asian_countries() == ["JP", "IN"]

assert len(match_asian_cities_pos()) == 2

assert match_asian_countries_pos() == ["JP", "IN"]


assert City.__match_args__ == ("continent", "name", "country")
