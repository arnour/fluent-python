from collections.abc import Sequence
from random import shuffle
from typing import TypeVar

T = TypeVar("T")


def sample(population: Sequence[T], size: int) -> Sequence[T]:
    if size < 1:
        raise ValueError("size must be >= 1")
    result = list(population)
    shuffle(result)
    return result[:size]


my_sample = sample([1, 2, 3], 2)

assert set(my_sample).issubset([1, 2, 3])
assert len(my_sample) == 2

my_other_sample = sample((4, 5, 6, 7), 3)

assert set(my_other_sample).issubset(set((4, 5, 6, 7)))
assert len(my_other_sample) == 3
