# same text encoded as three different byte sequences

s = 'El Niño'

for codec in ['latin_1', 'utf_8', 'utf_16']:
    print(codec, s.encode(codec), sep='\t')
    
latin_1 =s.encode('latin_1')

assert latin_1 == b'El Ni\xf1o'    
assert len(latin_1) == 7

utf_8 =s.encode('utf_8')

assert utf_8 == b'El Ni\xc3\xb1o'    
assert len(utf_8) == 8

utf_16 =s.encode('utf_16')

assert utf_16 == b'\xff\xfeE\x00l\x00 \x00N\x00i\x00\xf1\x00o\x00'    
assert len(utf_16) == 16