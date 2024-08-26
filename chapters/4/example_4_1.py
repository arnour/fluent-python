# Encoding and decoding

s = 'café'

assert len(s) == 4

b = s.encode('utf8')

assert b == b'caf\xc3\xa9'

assert len(b) == 5

assert b.decode('utf8') == s