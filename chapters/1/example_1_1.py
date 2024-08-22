# A Pythonic Card Deck

from collections import namedtuple
from typing import List, LiteralString
from random import choice

Card = namedtuple("Card", ["rank", "suit"])

suite_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)


def spades_high(card: Card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suite_values) + suite_values[card.suit]


class FrenchDeck:
    ranks: List[str] = [str(n) for n in range(2, 11)] + list("JQKA")
    suits: List[LiteralString] = "spades diamonds clubs hearts".split()

    def __init__(self) -> None:
        self._cards: List[Card] = [
            Card(rank, suit) for suit in self.suits for rank in self.ranks
        ]

    def __len__(self) -> int:
        return len(self._cards)

    def __getitem__(self, position) -> Card:
        return self._cards[position]


deck = FrenchDeck()

# counting the collection
assert len(deck) == 52, "The french deck should have 52 cards"

# accessing a position in the collection
assert deck[0] == Card(
    rank="2", suit="spades"
), "The first card in the deck should be 2 of spades"

# slicing the collection
assert deck[3:5] == [
    Card(rank="5", suit="spades"),
    Card(rank="6", suit="spades"),
], "This slice should contain 5 and 6 of spades"

# picking a random card
assert choice(deck) in deck, "The choice should belong to the deck"

# picking just aces using slicing (starting at index 12 and skipping 13 cards at a time)
assert deck[12::13] == [
    Card(rank="A", suit="spades"),
    Card(rank="A", suit="diamonds"),
    Card(rank="A", suit="clubs"),
    Card(rank="A", suit="hearts"),
], "This slice should contain all aces"

# iterate over the collection
assert [int(card.rank) for card in deck[0:5]] == list(
    range(2, 7)
), "Iterate over the first five items in the deck"

# iterate over the reversed collection
assert [int(card.rank) for card in reversed(deck[0:5])] == list(
    range(6, 1, -1)
), "Iterate over the first reversed five items in the deck"


# sort the collection using spades_high (sort by rank, suit)
assert [card for card in sorted(iter(deck), key=spades_high)[:4]] == [
    Card(rank="2", suit="clubs"),
    Card(rank="2", suit="diamonds"),
    Card(rank="2", suit="hearts"),
    Card(rank="2", suit="spades")
    
], "This slice should contains sorted cards by suites accordingly to spades_high"
