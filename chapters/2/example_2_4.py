# Cartesian product using a list comprehension

from typing import List, Tuple

colors: List[str] = ["black", "white"]
sizes: List[str] = ["S", "M", "L"]

tshirts: List[Tuple[str, str]] = [(color, size) for color in colors for size in sizes]

assert len(tshirts) == 6, "The cartesian product of colors and sizes has 6 elements"
assert tshirts == [
    ("black", "S"),
    ("black", "M"),
    ("black", "L"),
    ("white", "S"),
    ("white", "M"),
    ("white", "L"),
], "All color/size combinations should be present"
