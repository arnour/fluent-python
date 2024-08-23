# List Comprehensions and Readability

from typing import LiteralString, List

# Build a list of Unicode code points from a string, using a listcomp
symbols: LiteralString = "$¢£¥€¤"
codes: List[int] = [ord(symbol) for symbol in symbols]

assert codes == [36, 162, 163, 165, 8364, 164], "The unicode array for the string"
