# Initializing bytes from the raw data of an array

import array

# Typecode 'h' creates an array of short integers (16 bits).
numbers = array.array('h', [-2, -1, 0, 1, 2])

# octets holds a copy of the bytes that make up numbers.
octets = bytes(numbers)

# These are the 10 bytes that represent the 5 short integers.
assert octets == b'\xfe\xff\xff\xff\x00\x00\x01\x00\x02\x00'

assert len(octets) == 10
