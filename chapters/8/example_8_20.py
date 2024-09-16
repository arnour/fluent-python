from typing import Protocol, Any, TypeVar, TYPE_CHECKING
from collections.abc import Iterable, Iterator
import pytest


class SupportsLessThan(Protocol):
    def __lt__(self, other) -> bool: ...


LT = TypeVar("LT", bound=SupportsLessThan)


class Spam:
    def __init__(self, n) -> None:
        self.n = n

    def __lt__(self, other) -> bool:
        return self.n < other.n

    def __repr__(self) -> str:
        return f"Spam({self.n})"


def top(series: Iterable[LT], length: int) -> list[LT]:
    ordered = sorted(series, reverse=True)
    return ordered[:length]


def test_top_tuples() -> None:
    fruits = "mango pear apple kiwi banana".split()
    series: Iterator[tuple[int, str]] = ((len(fruit), fruit) for fruit in fruits)
    length = 3
    expected = [(6, "banana"), (5, "mango"), (5, "apple")]
    result = top(series, length)
    # The typing.TYPE_CHECKING constant is always False at runtime,
    # but type checkers pretend it is True when they are type checking
    # This if prevents the next three lines from executing when the test runs
    if TYPE_CHECKING:
        # reveal_type() cannot be called at runtime, because it is not a regular function but a Mypy debugging facility—that’s why there is no import for it.
        reveal_type(series)
        reveal_type(expected)
        reveal_type(result)
    assert result == expected


def test_top_objects_error() -> None:
    series = [object() for _ in range(4)]
    # The typing.TYPE_CHECKING constant is always False at runtime,
    # but type checkers pretend it is True when they are type checking
    if TYPE_CHECKING:
        # reveal_type() cannot be called at runtime, because it is not a regular function but a Mypy debugging facility—that’s why there is no import for it.
        reveal_type(series)
    with pytest.raises(TypeError) as err:
        top(series, 3)
    assert "'<' not supported" in str(err.value)
