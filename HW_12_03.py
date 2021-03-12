class SparseList:
    def __init__(self):
        self._data = {}
        self._len = 0

    def __repr__(self):  # переписать: вписать из словаря значения по ключу for k, v in s._d.it(): temp[k] = v
        temp = [0.] * self._len
        for i in range(len(self)):
            if i in self._data.keys():
                temp.append(self._data[i])
            else:
                temp.append(0)
        return str(temp)

    def __len__(self):
        return self._len

    def __setitem__(self, key, value):  # переписать отриц индескы в нормальные
        # d[] = v +
        if not isinstance(key, int) and not isinstance(value, (float, int)):
            raise TypeError
        if key >= self._len:
            raise IndexError("list index out of range")
        elif key < -self._len:
            raise IndexError("list assignment index out of range")
        elif -self._len <= key < 0:
            if value == 0:
                del self._data[self._len + key]
            else:
                self._data[self._len + key] = value
        else:
            if value == 0:
                try:
                    del self._data[key]
                except KeyError:
                    pass
            else:
                self._data[key] = value

    def __getitem__(self, item):  # переписать
        # v = d[] +
        if isinstance(item, int):
            if item >= self._len or -self._len > item:
                raise IndexError('list index out of range')
            if 0 <= item < self._len:
                try:
                    return self._data[item]
                except KeyError:
                    return 0.
            elif isinstance(item, int) and item >= -self._len:
                try:
                    return self._data[len(self) + item]
                except KeyError:
                    return 0
        elif isinstance(item, slice):
            out_dict = SparseList()
            for i in range(*item.indices(len(self))):
                try:
                    out_dict._data[i] = self._data[i]
                    out_dict._len += 1
                except KeyError:
                    out_dict._len += 1
            return out_dict
        else:
            raise TypeError

    def __delitem__(self, key):  # переписать срез и преобразовать отрицательные индескы
        # del o[]
        if not isinstance(key, (int, slice)):
            raise TypeError
        new_obj = SparseList()
        if isinstance(key, int):
            if key < -len(self):
                raise IndexError("list index out of range")
            if key >= self._len:  # or key < -self._len
                raise IndexError("list index out of range")

            if 0 <= key:
                try:
                    del self._data[key]
                except KeyError:
                    ...
                for i in range(len(self)):
                    if i in self._data.keys():
                        if key > i:
                            new_obj._data[i] = self._data[i]
                        else:
                            new_obj._data[i-1] = self._data[i]
                self._len -= 1
            elif -len(self) <= key:
                try:
                    del self._data[key + len(self)]
                except KeyError:
                    ...
                for i in range(len(self)):
                    if i in self._data.keys():
                        if key + len(self) > i:
                            # print(i, key)
                            new_obj._data[i] = self._data[i]
                        else:
                            new_obj._data[i - 1] = self._data[i]
                self._len -= 1

        elif isinstance(key, slice):
            for i in range(*key.indices(len(self))):
                try:
                    del self._data[i]
                except KeyError:
                    pass
            inter = (key.stop - key.start) // key.step
            for i in range(len(self)):
                if i < key.start:
                    new_obj._data[i] = self._data[i]
                elif key.stop < i:
                    new_obj._data[i - inter] = self._data[i]
            self._len -= inter
        else:
            raise TypeError
        self._data = new_obj._data

    def append(self, item):
        if not isinstance(item, (float, int)):
            raise ValueError
        elif item == 0:
            self._len += 1
        else:
            self._data[self._len] = item
            self._len += 1

    def pop(self, index=None):  # переписать
        if isinstance(index, type(None)):
            try:
                value = self[self._len - 1]
                del self[self._len - 1]
            except KeyError:
                self._len -= 1
                return 0
        elif not isinstance(index, int):
            raise TypeError(f"{type(index)} object cannot be interpreted as an integer")
        elif index >= self._len or index < -self._len:
            raise IndexError("pop index out of range")
        else:
            try:
                value = self[index]
                del self[index]
            except KeyError:
                ...
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

    def index(self, item):  # дописать старт, стоп
        if not isinstance(item, (int, float)):
            raise TypeError
        elif item == 0:
            if len(self) == len(self._data):
                raise ValueError
            else:
                for i in range(len(self)):
                    try:
                        self._data[i]
                    except KeyError:
                        return i
        for key, val in self._data.items():
            if val == item:
                return key
            raise ValueError

    def remove(self, item):  # переписать понять чем это функция отличается
        del self[item]

    def reverse(self):
        new_list = {}
        ln = self._len - 1
        for key, vals in self._data.items():
            new_list[ln - key] = vals
        self._data = new_list


test = SparseList()
test.pop()
test.append(2)
test.append(1)
test.append(0)
test.append(3)
test.append(6)
test.append(5)
test.append(6)
print(test._data)
print(test)
test.pop(-1)
# print(test.count(0))
test.extend([1, 0, 4])

print(test)
test.reverse()
print(test)


