# Sorting a list of words by their reversed spelling using lambda

fruits = ["strawberry", "fig", "apple", "cherry", "raspberry", "banana"]

assert sorted(fruits, key=lambda word: word[::-1]) == [
    "banana",
    "apple",
    "fig",
    "raspberry",
    "strawberry",
    "cherry",
]
