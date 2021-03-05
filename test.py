# 5_03
from collections.abc import MutableMapping


class DickLike(MutableMapping):
    def __len__(self) -> int:
        pass

    def __iter__(self):
        ...

    def __init__(self):
        self._data = {}

    def __getitem__(self, item):
        # v = d[]
        return self._data[item]

    def __setitem__(self, key, value):
        # d[] = v
        if not isinstance(key, int):
            raise TypeError
        elif key < 1:
            raise ValueError
        self._data[key] = value

    def __delitem__(self, key):
        # del o[]
        del self._data[key]

    def get(self, key, default=None, /):
        try:
            return self[key]
        except KeyError:
            return default

    def __contains__(self, item):
        try:
            self[item]
        except KeyError:
            return False
        return True

    def setdefault(self, key, default=None, /):
        try:
            return self[key]
        except KeyError:
            self[key] = default
            return default


d = DickLike()
d[3] = 4
print(d._data)
print(d.get(1))
print(d.get(1, 2))
print(1 in d)
print(3 in d)
print(d.setdefault(3))
print(d.setdefault(2))
# д\з ключи название файлов, в инит путь до директории, занчение содержимое файла,
# если название файла, папка то вернуть словарь

# какой-то другой день

# def g():
#     print("1")
#     yield 2
#     print("3")

# g = iter(ol)  # он помнит что остановился
# for n in g:  # аналогично for n in ol:
#     ...


# for n in x:
#   ...
# while True:
#     try:
#         n = next(x)
#     except StopIteration:
#         break
#     else:
#         ...

    # def iterr_bonds(self):
    #     # Значения выглядят как матрица смежности и бежим по элементам главной диагонали и над ней. Работает только
    #     # если атомы попорядку
    #     bonds_size = len(self._bonds)
    #     for i in range(bonds_size):
    #         for j in range(bonds_size - i):
    #             j += i
    #             try:
    #                 _ = self._bonds[i + 1][j + 1]
    #                 yield i + 1, j + 1
    #             except KeyError:
    #                 continue

# x = g()
# print("Start")
# print(next(x))
# print("next")
# # print(next(x))
# # print("stop")

# print(hash(-3))
# print(hash(-1))
# print(hash(0))
# print(hash(1))
# print(hash(2))
#
# s = {1: (2, 3, 4)}

