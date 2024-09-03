# variables as boxes

a = [1, 2, 3]

b = a

a.append(4)

# Variables a and b hold references to the same list, not copies of the list
assert b == [1, 2, 3, 4]
