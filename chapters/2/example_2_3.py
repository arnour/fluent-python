# Listcomps Versus map and filter

from typing import LiteralString, List

# built by a listcomp
symbols: LiteralString = "$¢£¥€¤"
beyond_ascii: List[int] = [ord(symbol) for symbol in symbols if ord(symbol) > 127]

assert beyond_ascii == [162, 163, 165, 8364, 164], "The unicode array for the string beyond ascii"

# built by map/filter
beyond_ascii: List[int] = list(filter(lambda o: o > 127, map(ord, symbols)))

assert beyond_ascii == [162, 163, 165, 8364, 164], "The unicode array for the string beyond ascii"