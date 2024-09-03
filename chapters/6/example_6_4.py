# alex and charles compare equal, but alex is not charles

charles = {"name": "Charles L. Dodgson", "born": 1932}

alex = {"name": "Charles L. Dodgson", "born": 1932}

# alex refers to an object that is a replica of the object assigned to charles. 
# The objects compare equal because of the __eq__ implementation in the dict class
assert alex == charles

# But they are distinct objects. 
# This is the Pythonic way of writing the negative identity comparison: a is not b
assert alex is not charles

#  The objects bound to alex and charles have the same value
#  that’s what == compares—but they have different identities