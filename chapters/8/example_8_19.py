from collections.abc import Iterable
from typing import TypeVar

T = TypeVar("T")


def top(series: Iterable[T], length: int) -> list[T]:
    ordered = sorted(series, reverse=True)
    return ordered[:length]


assert top([4, 1, 5, 2, 6, 7, 3], 3) == [7, 6, 5]
assert top("mango pear apple kiwi banana".split(), 3) == ["pear", "mango", "kiwi"]
assert top([(len(f), f) for f in "mango pear apple kiwi banana".split()], 3) == [(6, 'banana'), (5, 'mango'), (5, 'apple')]
