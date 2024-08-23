# Pattern Matching with Mappings: get_creators() extracts names of creators from media records
from typing import List
from collections import OrderedDict


def get_creators(record: dict) -> List[str]:
    match record:
        case {"type": "book", "api": 2, "authors": [*names]}:
            return names
        case {"type": "book", "api": 1, "author": name}:
            return [name]
        case {"type": "book"}:
            raise ValueError(f"Invalid 'book' record: {record!r}")
        case {"type": "movie", "director": name}:
            return [name]
        case _:
            raise ValueError(f"Invalid record: {record!r}")


b1 = dict(api=1, author="Douglas Hofstadter", type="book", title="Gödel, Escher, Bach")

assert get_creators(b1) == ["Douglas Hofstadter"]

b2 = OrderedDict(
    api=2,
    type="book",
    title="Python in a Nutshell",
    authors="Martelli Ravenscroft Holden".split(),
)

assert get_creators(b2) == ["Martelli", "Ravenscroft", "Holden"]

try:
    get_creators({"type": "book", "pages": 770})
except ValueError as err:
    assert str(err) == "Invalid 'book' record: {'type': 'book', 'pages': 770}"


try:
    get_creators({1: "Spam, spam, spam"})
except ValueError as err:
    assert str(err) == "Invalid record: {1: 'Spam, spam, spam'}"
