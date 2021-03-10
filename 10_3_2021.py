class DictLike:
    def __init__(self):
        self._data = {}

    def __getitem__(self, item):
        if isinstance(item, int):
            return self._data[item]
        elif isinstance(item, slice):
            out_dict = {}
            for i in range(*item.indices(max(self._data))):
                try:
                    self[i]
                except KeyError:
                    pass
                else:
                    out_dict[i] = self[i]
            return out_dict
        else:
            raise TypeError

    def __setitem__(self, key, value):
        # d[] = v
        if not isinstance(key, int):
            raise TypeError
        elif key < 1:
            raise ValueError
        self._data[key] = value

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

