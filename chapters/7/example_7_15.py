# Demo of methodcaller: second test shows the binding of extra arguments

from operator import methodcaller

s = 'The time has come'

upcase = methodcaller('upper')

assert upcase(s) == 'THE TIME HAS COME'

hyphenate = methodcaller('replace', ' ', '-')

assert hyphenate(s) == 'The-time-has-come'