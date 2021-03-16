class SparseList:
    def __init__(self):
        self._data = {}
        self._len = 0

    def __repr__(self):
        temp = [0.] * self._len
        for k, v in self._data.items():
            temp[k] = v
        return str(temp)

    def __len__(self):
        return self._len

    def __setitem__(self, key, value):
        # d[] = v +
        if not isinstance(key, int) and not isinstance(value, (float, int)):
            raise TypeError
        elif key >= self._len:
            raise IndexError("list index out of range")
        elif key < -self._len:
            raise IndexError("list assignment index out of range")
        elif -self._len <= key < 0:
            key = self._len + key
        if value == 0:
            try:
                del self._data[key]
            except KeyError:
                pass
        else:
            self._data[key] = value

    def __getitem__(self, item):
        # v = d[] +
        if isinstance(item, int):
            if item >= self._len or -self._len > item:
                raise IndexError('list index out of range')
            elif item < 0:
                item = self._len + item
            return self._data.get(item, 0.)
        elif isinstance(item, slice):
            out_dict = SparseList()
            for i in range(*item.indices(len(self))):
                try:
                    out_dict._data[out_dict._len] = self._data[i]
                    out_dict._len += 1
                except KeyError:
                    out_dict._len += 1
            return out_dict
        else:
            raise TypeError

    def __delitem__(self, key):
        # del o[]
        if not isinstance(key, (int, slice)):
            raise TypeError
        new_obj = SparseList()
        if isinstance(key, int):
            if key >= self._len or key < -self._len:
                raise IndexError("list index out of range")
            if key < 0:
                key = self._len + key
            try:
                del self._data[key]
            except KeyError:
                ...
            for i in range(self._len):
                if i in self._data.keys():
                    if key > i:
                        new_obj._data[i] = self._data[i]
                    else:
                        new_obj._data[i-1] = self._data[i]
            self._len -= 1
            self._data = new_obj._data
        elif isinstance(key, slice):
            indicies_to_del = []
            for i in range(*key.indices(self._len)):
                indicies_to_del.append(i)  # список элементов в слайсе
            while len(indicies_to_del) > 0:
                idx = indicies_to_del.pop()
                del self[idx]
        else:
            raise TypeError

    def append(self, item):
        if not isinstance(item, (float, int)):
            raise ValueError
        elif item == 0:
            self._len += 1
        else:
            self._data[self._len] = item
            self._len += 1

    def pop(self, index=None):
        if isinstance(index, type(None)):
            try:
                value = self[self._len - 1]
                del self[self._len - 1]
            except KeyError:
                self._len -= 1
                return 0.
        elif not isinstance(index, int):
            raise TypeError(f"{type(index)} object cannot be interpreted as an integer")
        elif index >= self._len or index < -self._len:
            raise IndexError("pop index out of range")
        else:
            try:
                value = self[index]
                del self[index]
            except KeyError:
                return 0.
        return value

    def count(self, item):
        if not isinstance(item, (int, float)):
            raise TypeError
        elif item == 0:
            return len(self) - len(self._data)
        else:
            temp = 0
            for i in self._data.values():
                if item == i:
                    temp += 1
            return sum(v == item for v in self._data.values())

    def clear(self):
        self._data = {}
        self._len = 0

    def extend(self, item):
        for i in item:
            self.append(i)

    def index(self, item, start=0, stop=2147483647):
        if not isinstance(item, (int, float)):
            raise TypeError
        elif start >= self._len:
            raise ValueError
        elif item == 0.:
            if len(self) == len(self._data):
                raise ValueError
            else:
                for i in range(start, len(self)):
                    try:
                        self._data[i]
                    except KeyError:
                        return i
                raise ValueError
        else:
            for key, val in self._data.items():
                if start <= key < stop:
                    if val == item:
                        return key
            else:
                raise ValueError

    def remove(self, item):
        if not isinstance(item, (int, float)):
            raise TypeError
        del self[self.index(item)]

    def reverse(self):
        new_list = {}
        ln = self._len - 1
        for key, vals in self._data.items():
            new_list[ln - key] = vals
        self._data = new_list

    def insert(self, index, object):
        if not isinstance(index, int):
            raise TypeError
        elif not isinstance(object, (int, float)):
            raise TypeError
        elif index >= self._len:
            print("app")
            self.append(object)
        else:
            if index < -self._len:
                index = 0
            elif index < 0:
                index += self._len
            temp_dict = SparseList()
            if index == 0:
                if object != 0.:
                    temp_dict._data[0] = object
                for ind, val in self._data.items():
                    temp_dict._data[ind + 1] = val
            else:
                for ind, val in self._data.items():
                    if index > ind:
                        temp_dict._data[ind] = val
                    elif index == ind:
                        if object != 0.:
                            temp_dict._data[ind] = object
                        temp_dict._data[ind + 1] = val
                    else:
                        temp_dict._data[ind + 1] = val
            self._data = temp_dict._data
            self._len += 1

    def copy(self):
        new = SparseList()
        new._data = self._data.copy()
        new._len = self._len
        return new


test = SparseList()
# test.pop()
test.append(2.)
test.append(1.)
test.append(0.)
test.append(0.)
test.append(0.)
test.append(0.)
test.append(6.)
test.append(5.)
test.append(7.)
test[3] = 3.
print(test)
del test[2:7:2]
print(test)
print([2., 1., 3., 0., 5., 7.])
test.remove(0.)
print(test)
test.insert(-4, 454.0)
print(test)
