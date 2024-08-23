# StrKeyDict0 converts nonstring keys to str on lookup


class StrKeyDict0(dict):

    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def get(self, key, default=None):
        try:
            self[key]
        except KeyError:
            return default

    def __contains__(self, key: object) -> bool:
        return key in self.keys() or str(key) in self.keys()


d = StrKeyDict0([('1', 2), (3, 4)])

assert d[1] == 2

assert d['1'] == 2

assert 1 in d