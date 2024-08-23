# Set Comprehensions

from unicodedata import name

chars = {(chr(i), name(chr(i), "")) for i in range(32, 256) if "SIGN" in name(chr(i), "")}

assert len(chars) == 21