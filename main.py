from random import gauss


class RandomFloat:
    def __init__(self, mu: float, /, *, sigma: float = 1.):
        if not isinstance(mu, float) or not isinstance(sigma, float):
            raise TypeError
        self.mu = mu
        self.sigma = sigma
        self.old = 0

    def is_numeric(self, other):
        if isinstance(other, RandomFloat):
            other = float(other)
        elif not isinstance(other, (float, int)):
            raise TypeError
        return other

    def __float__(self):
        return gauss(self.mu, self.sigma)

    def __int__(self):
        return int(float(self))

    def __add__(self, other):
        other = self.is_numeric(other)
        return float(self) + other

    def __radd__(self, other):
        return self + other

    # def __iadd__(self, other):
    #     if self.old == 0:
    #         self.old = self + other
    #         return self + other
    #     else:
    #         self.old += other
    #         return self.old

    def __mul__(self, other):
        other = self.is_numeric(other)
        return float(self) * other

    def __rmul__(self, other):
        return self * other

    def __imul__(self, other):
        if self.old == 0:
            self.old = self * other
            return self * other
        else:
            self.old *= other
            return self.old

    def __sub__(self, other):
        other = self.is_numeric(other)
        return float(self) - other

    def __rsub__(self, other):
        return -(self - other)

    def __isub__(self, other):
        if self.old == 0:
            self.old = self - other
            return self - other
        else:
            self.old -= other
            return self.old

    def __abs__(self):
        return abs(float(self))

    def __truediv__(self, other):
        other = self.is_numeric(other)
        return float(self) / other

    def __rtruediv__(self, other):
        other = self.is_numeric(other)
        return other / float(self)

    def __itruediv__(self, other):
        if self.old == 0:
            self.old = self / other
            return self / other
        else:
            self.old /= other
            return self.old

    def __floordiv__(self, other):
        other = self.is_numeric(other)
        return int(float(self) / other)

    def __rfloordiv__(self, other):
        other = self.is_numeric(other)
        return int(other / float(self))

    def __ifloordiv__(self, other):
        self.is_numeric(other)
        if self.old == 0:
            self.old = self // other
            return self // other
        else:
            self.old //= other
            return self.old

    def __mod__(self, other):
        other = self.is_numeric(other)
        return float(self) % other

    def __rmod__(self, other):
        return other % float(self)

    def __imod__(self, other):
        if self.old == 0:
            self.old = self % other
            return self % other
        else:
            self.old %= other
            return self.old

    def __pow__(self, power, modulo=None):
        self.is_numeric(power)
        return float(self) ** power

    def __rpow__(self, other):
        other = self.is_numeric(other)
        return other ** float(self)

    def __ipow__(self, other):
        if self.old == 0:
            self.old = self ** other
            return self ** other
        else:
            self.old **= other
            return self.old

    def __iadd__(self, other):
        if isinstance(other, RandomFloat):
            return RandomFloat(self.mu + other)
        elif not isinstance(other, float):
            raise TypeError
        return RandomFloat(self.mu + other)


# <, >, =<, =>, через float
# == RandomFloat(10.0) и RandomFloat(10.0) скастовать в float и сравнивать как число и RF, RandomFloat(10.0) и
# число: float(RandomFloat(10.0)) - число = +_ 0.001 (погрешность). Добавить настройку погрешности для класса.
c = RandomFloat(10.0)
print(c)
c += 1.
print(c)
