# Encoding to bytes: success and error handling

city = "São Paulo"

# The UTF encodings handle any str.

assert city.encode("utf8") == b"S\xc3\xa3o Paulo"

assert (
    city.encode("utf16") == b"\xff\xfeS\x00\xe3\x00o\x00 \x00P\x00a\x00u\x00l\x00o\x00"
)

# iso8859_1 also works for the 'São Paulo' string

assert city.encode("iso8859_1") == b"S\xe3o Paulo"

# cp437 can’t encode the 'ã' (“a” with tilde). The default error handler—'strict'—raises UnicodeEncodeError
try:
    city.encode("cp437")
except UnicodeEncodeError as err:
    assert (
        err.reason
        == "character maps to <undefined>"
    )

# The error='ignore' handler skips characters that cannot be encoded; this is usually a very bad idea, leading to silent data loss
assert city.encode('cp437', errors='ignore') == b'So Paulo'

# When encoding, error='replace' substitutes unencodable characters with '?'; data is also lost, but users will get a clue that something is amiss
assert city.encode('cp437', errors='replace') == b'S?o Paulo'

# 'xmlcharrefreplace' replaces unencodable characters with an XML entity. If you can’t use UTF, and you can’t afford to lose data, this is the only option.
assert city.encode('cp437', errors='xmlcharrefreplace') == b'S&#227;o Paulo'



