# Handling 6 bytes of memory as 1×6, 2×3, and 3×2 views

from array import array

# Build array of 6 bytes (typecode 'B')
octets = array('B', range(6))

# Build memoryview from that array, then export it as a list.
m1 = memoryview(octets)

print(m1.tolist())

# Build new memoryview from that previous one, but with 2 rows and 3 columns.
m2 = m1.cast('B', [2, 3])

print(m2.tolist())

# Yet another memoryview, now with 3 rows and 2 columns.
m3 = m1.cast('B', [3, 2])

print(m3.tolist())

# Overwrite byte in m2 at row 1, column 1 with 22
m2[1,1] = 22

# Overwrite byte in m3 at row 1, column 1 with 33
m3[1,1] = 33

# Display original array, proving that the memory was shared among octets, m1, m2, and m3.
print(octets)

assert octets == array('B', [0, 1, 2, 33, 22, 5])