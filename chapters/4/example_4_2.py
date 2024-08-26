# A five-byte sequence as bytes and as bytearray
cafe = bytes('café', encoding='utf8')

assert cafe == b'caf\xc3\xa9'

assert len(cafe) == 5

assert cafe[0] == 99

# Slices of bytes are also bytes—even slices of a single byte
assert cafe[:1] == b'c'

# There is no literal syntax for bytearray: they are shown as bytearray() with a bytes literal as argument.
cafe_arr = bytearray(cafe)

assert len(cafe_arr) == 5

# A slice of bytearray is also a bytearray
assert cafe_arr[-1:] == bytearray(b'\xa9')