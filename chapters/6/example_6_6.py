# Making a shallow copy of a list containing another list; copy and paste this code to see it animated at the Online Python Tutor

l1 = [3, [66, 55, 44], (7, 8, 9)]
l2 = list(l1)

# Appending 100 to l1 has no effect on l2
l1.append(100)

# Here we remove 55 from the inner list l1[1]. This affects l2 because l2[1] is bound to the same list as l1[1].
l1[1].remove(55)

# l2 is a shallow copy of l1
assert l1 is not l2
assert l1 != l2

assert l1[1] is l2[1]

# For a mutable object like the list referred by l2[1], the operator += changes the list in place. This change is visible at l1[1], which is an alias for l2[1].
l2[1] += [33, 22]

# += on a tuple creates a new tuple and rebinds the variable l2[2] here.
# This is the same as doing l2[2] = l2[2] + (10, 11).
# Now the tuples in the last position of l1 and l2 are no longer the same object
l2[2] += (10, 11)


assert l1[2] != l2[2]
assert l1[2] is not l2[2]
