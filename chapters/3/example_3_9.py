# Subclassing UserDict Instead of dict
import collections

class StrKeyDict(collections.UserDict):
    
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def __contains__(self, key: object) -> bool:
        # we can assume all stored keys are str, and we can check on self.data
        return str(key) in self.data
    
    def __setitem__(self, key, item) -> None:
        # converts any key to a str
        self.data[str(key)] = item
        
d = StrKeyDict([(1, 2), (3, 4), (5, 6)])

assert d['1'] == 2

assert d[1] == 2

assert '1' in d

d[7] = 8

assert '7' in d