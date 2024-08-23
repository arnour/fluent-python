# Generator Expressions

from typing import LiteralString, List
import array

symbols: LiteralString = "$¢£¥€¤"

# Initializing a tuple from a generator expression
codes = tuple(ord(symbol) for symbol in symbols)

assert codes == (36, 162, 163, 165, 8364, 164), "The unicode tuple for the string"

# Initializing an array from a generator expression
codes = array.array('I', (ord(symbol) for symbol in symbols))

assert codes == array.array('I', [36, 162, 163, 165, 8364, 164]), "The unicode array for the string"