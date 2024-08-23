# MappingProxyType builds a read-only mappingproxy instance from a dict

from types import MappingProxyType

d = {1: "A"}

d_proxy = MappingProxyType(d)

assert d == d_proxy

assert d_proxy[1] == "A"

try:
    d_proxy[2] = "x"
except TypeError as err:
    assert str(err) == "'mappingproxy' object does not support item assignment"


d[2] = 'B'

assert d_proxy[2] == 'B'