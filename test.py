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


x = g()
print("Start")
print(next(x))
print("next")
print(next(x))
print("stop")
