#  Sorting a list of words by length

fruits: list[str] = ["strawberry", "fig", "apple", "cherry", "raspberry", "banana"]

assert sorted(fruits, key=len) == ["fig", "apple", "cherry", "banana", "raspberry", "strawberry"]
