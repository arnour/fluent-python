# Creating, saving, and loading a large array of floats

from array import array
from random import random

floats = array('d', (random() for _ in range(10**7)))

with open('floats.bin', 'wb') as f:
    floats.tofile(f)

floats2 = array('d')

with open('floats.bin', 'rb') as f:
    floats2.fromfile(f, 10**7)

assert floats == floats2, 'The two array are identical'

