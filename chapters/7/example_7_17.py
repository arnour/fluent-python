# Building a convenient Unicode normalizing function with partial

import unicodedata, functools

nfc = functools.partial(unicodedata.normalize, 'NFC')

s1 = 'café'
s2 = 'cafe\u0301'

assert s1 != s2
assert nfc(s1) == nfc(s2)
