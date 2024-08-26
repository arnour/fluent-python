# Decoding from str to bytes: success and error handling

# The word “Montréal” encoded as latin1; '\xe9' is the byte for “é”.
octets = b"Montr\xe9al"

# Decoding with Windows 1252 works because it is a superset of latin1
assert octets.decode("cp1252") == "Montréal"

# ISO-8859-7 is intended for Greek, so the '\xe9' byte is misinterpreted, and no error is issued
assert octets.decode("iso8859_7") == "Montrιal"

# KOI8-R is for Russian. Now '\xe9' stands for the Cyrillic letter “И”
assert octets.decode("koi8_r") == "MontrИal"

# The 'utf_8' codec detects that octets is not valid UTF-8, and raises UnicodeDecodeError
try:
    assert octets.decode("utf_8") == "Montrιal"
except UnicodeDecodeError as err:
    assert err.reason == "invalid continuation byte"

# Using 'replace' error handling, the \xe9 is replaced by “�” (code point U+FFFD), the official Unicode REPLACEMENT CHARACTER intended to represent unknown characters.
assert octets.decode("utf_8", errors="replace") == "Montr�al"