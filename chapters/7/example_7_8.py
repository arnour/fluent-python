# A BingoCage does one thing: picks items from a shuffled list
import random


class BingoCage:

    def __init__(self, items) -> None:
        self._items = list(items)
        random.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError("pick from empty bingo cage")

    def __call__(self):
        return self.pick()


bingo = BingoCage(range(3))

assert bingo.pick() in range(3)

assert bingo() in range(3)

assert callable(bingo)
