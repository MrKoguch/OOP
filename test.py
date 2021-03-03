def g():
    print("1")
    yield 2
    print("3")

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

print(hash(-3))
print(hash(-1))
print(hash(0))
print(hash(1))
print(hash(2))

s = {1: (2, 3, 4)}
