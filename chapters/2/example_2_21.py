# Changing the value of a 16-bit integer array item by poking one of its bytes

import array

# Build memoryview from array of 5 16-bit signed integers (typecode 'h')
numbers = array.array('h', [-2, -1, 0, 1, 2])

memv = memoryview(numbers)

# memv sees the same 5 items in the array
assert len(memv) == 5

assert memv[0] == -2

# Create memv_oct by casting the elements of memv to bytes (typecode 'B')
memv_oct = memv.cast('B')

# Assign value 4 to byte offset 5
memv_oct[5] = 4

# Note the change to numbers: a 4 in the most significant byte of a 2-byte unsigned integer is 1024
assert numbers == array.array('h', [-2, -1, 1024, 1, 2])