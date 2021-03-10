class DictLike:
    def __init__(self):
        self._data = {}

    def __setitem__(self, key, value):
        # d[] = v
        if not isinstance(key, int):
            raise TypeError
        elif key < 1:
            raise ValueError
        self._data[key] = value

    def __getitem__(self, item):
        if isinstance(item, int):
            return self._data[item]
        elif isinstance(item, slice):
            out_dict = DictLike()
            for i in range(*item.indices(max(self._data))):
                try:
                    out_dict[i] = self._data[i]
                except KeyError:
                    pass
            return out_dict
        else:
            raise TypeError

    def __delitem__(self, key):
        if isinstance(key, int):
            del self._data[key]
        elif isinstance(key, slice):
            for i in range(*key.indices(max(self._data))):
                try:
                    del self[i]
                except KeyError:
                    pass
        else:
            raise TypeError
        # del o[]


d = DictLike()
d[1] = 1
d[2] = 2
d[3] = 3
d[4] = 4
d[5] = 5
print(d._data)
c = d[2:4]
print(c._data)
del d[2:4]
print(d._data)

