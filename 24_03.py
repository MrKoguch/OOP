# Замыкание
def c(b):
    def f(a):
        return a + b
    return f


x = c(1)
print(x(2))


# Декаратор
def d(f):  # Принимает на вход функцию
    def w(*args, **kwargs):  # (*args, **kwargs) - хавает все переданные в нее агрументы
        return f(*args, **kwargs)
    return w


import time


def d_t(f):  # Принимает на вход функцию
    def w(*args, **kwargs):  # (*args, **kwargs) - хавает все переданные в нее агрументы
        t = time.perf_counter()
        r = f(*args, **kwargs)
        print(time.perf_counter() - t)  # работает
        return r
    return w


# Декаратор и замыкание
def p(f, *args, **kwargs):  # принимает аргименты и функцию
    def w(*aa, **kk):
        f(*args, *aa, **kwargs, **kk)
    return w


def x(a, b):
    return a+b


y = p(x, 1)
y(2)   # = 3


# Равноудаленность от элемента

def x(a, b):  # a - центральное число для сортировки
    return abs(a - b)

# библиотека from functools import partial содержит нашу функцию p()


from functools import wraps
def c(*a, **k):  # замыкание
    def d(f):  # декаратор
        @ wraps(f)  # автоматически модифицирует функцию чтоб было видно как буд-то она не менялась
        def w(*aa, **kk):  # функция обертка
            return f(*a, *aa, **k, **kk)  # обертка функции
        # имитация того что функция не менялась
        # w.__doc__ = f.__doc__
        # w.__module__ = f.__module__
        # w.__qualname__ = f.__qualname__
        return w
    return d


@c(1)  # k = c(1)(k)
def k(a, b):
    '''
    k.__doc__()
    :param a: asd
    :param b: sda
    :return: asd
    '''
    return abs(a - b)



