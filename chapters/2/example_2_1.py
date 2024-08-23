# List Comprehensions and Readability

from typing import LiteralString

# Build a list of Unicode code points from a string

symbols: LiteralString = '$¢£¥€¤'
codes = []
for symbol in symbols:
    codes.append(ord(symbol))

assert codes == [36, 162, 163, 165, 8364, 164], 'The unicode array for the string'