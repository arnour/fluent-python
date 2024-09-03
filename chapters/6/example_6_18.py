# String literals may create shared objects

t1 = (1, 2, 3)
t3 = (1, 2, 3)

# should be different
# assert t3 is not t1

s1 = "ABC"
s2 = "ABC"

assert s1 is s2
