# Sorting a list of words by their reversed spelling


def reverse(word):
    return word[::-1]


assert reverse("testing") == "gnitset"

fruits: list[str] = ["strawberry", "fig", "apple", "cherry", "raspberry", "banana"]

assert sorted(fruits, key=reverse) == [
    "banana",
    "apple",
    "fig",
    "raspberry",
    "strawberry",
    "cherry",
]
