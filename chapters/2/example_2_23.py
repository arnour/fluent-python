# Working with a deque

from collections import deque

# The optional maxlen argument sets the maximum number of items allowed in this instance of deque; this sets a read-only maxlen instance attribute
dq = deque(range(10), maxlen=10)

assert dq == deque([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], maxlen=10), 'Deque should have max length equals to 10 and elements from 0 to 9'

# Rotating with n > 0 takes items from the right end and prepends them to the left
dq.rotate(3)

assert dq == deque([7, 8, 9, 0, 1, 2, 3, 4, 5, 6], maxlen=10), 'Last three elements should be put in the begining of the deque'

# when n < 0 items are taken from left and appended to the right.
dq.rotate(-4)

assert dq == deque([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], maxlen=10), 'First four elements should be put in the end of the deque'

# Appending to a deque that is full (len(d) == d.maxlen) discards items from the other end; note in the next line that the 0 is dropped.
dq.appendleft(-1)

assert dq == deque([-1, 1, 2, 3, 4, 5, 6, 7, 8, 9], maxlen=10), '-1 should be put in the begining of the deque and as side effect the last element should be removed to keep length'

# Adding three items to the right pushes out the leftmost -1, 1, and 2
dq.extend([11, 22, 33])

assert dq == deque([3, 4, 5, 6, 7, 8, 9, 11, 22, 33], maxlen=10), 'three new elements should be put in the end of the deque so the first three elements should be removed to keep length'

# Note that extendleft(iter) works by appending each successive item of the iter argument to the left of the deque, therefore the final position of the items is reversed.
dq.extendleft([10, 20, 30, 40])

assert dq == deque([40, 30, 20, 10, 3, 4, 5, 6, 7, 8], maxlen=10), 'four new elements should be put in the begining of the deque so the last four elements should be removed to keep length'

