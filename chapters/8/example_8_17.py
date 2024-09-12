from collections.abc import Iterable, Hashable
from collections import Counter
from typing import TypeVar
from decimal import Decimal
from fractions import Fraction


def mode(data: Iterable[float]) -> float:
    pairs = Counter(data).most_common(1)
    if len(pairs) == 0:
        raise ValueError("no mode for empty data")
    return pairs[0][0]


assert mode([1, 1, 2, 3, 3, 3, 3, 4]) == 3
assert mode([1, 2, 3]) == 1

# A restricted type variable will be set to one of the types named
# in the TypeVar declaration
NumberT = TypeVar("NumberT", float, Decimal, Fraction)


def typed_mode(data: Iterable[NumberT]) -> NumberT:
    pairs = Counter(data).most_common(1)
    if len(pairs) == 0:
        raise ValueError("no mode for empty data")
    return pairs[0][0]


assert typed_mode([1.1, 1.1, 2, 3, 3.3, 3.4, 3.5, 4]) == 1.1
assert typed_mode([1, 2.0, 3]) == 1

# A bounded type variable will be set to the inferred type of the expression—as
# long as the inferred type is consistent-with the boundary declared
# in the bound=keyword argument of TypeVar
HashableT = TypeVar("HashableT", bound=Hashable)


def hashable_mode(data: Iterable[HashableT]) -> HashableT:
    pairs = Counter(data).most_common(1)
    if len(pairs) == 0:
        raise ValueError("no mode for empty data")
    return pairs[0][0]


assert hashable_mode([1, 1, 2, 3, 3, 3, 3, 4]) == 3
assert hashable_mode(["red", "blue", "blue", "red", "green", "red", "red"]) == "red"
