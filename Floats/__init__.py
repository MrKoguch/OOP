from random import gauss


class CustomFloat:
    def is_numeric(self, other):
        if isinstance(other, CustomFloat):
            other = float(other)
        elif not isinstance(other, (float, int)):
            raise TypeError
        return other

    def __int__(self):
        return int(float(self))

    def __add__(self, other):
        other = self.is_numeric(other)
        return float(self) + other

    def __radd__(self, other):
        return self + other

    def __mul__(self, other):
        other = self.is_numeric(other)
        return float(self) * other

    def __rmul__(self, other):
        return self * other

    def __sub__(self, other):
        other = self.is_numeric(other)
        return float(self) - other

    def __rsub__(self, other):
        return -(self - other)

    def __abs__(self):
        return abs(float(self))

    def __truediv__(self, other):
        other = self.is_numeric(other)
        return float(self) / other

    def __rtruediv__(self, other):
        other = self.is_numeric(other)
        return other / float(self)

    def __floordiv__(self, other):
        other = self.is_numeric(other)
        return int(float(self) / other)

    def __rfloordiv__(self, other):
        other = self.is_numeric(other)
        return int(other / float(self))

    def __mod__(self, other):
        other = self.is_numeric(other)
        return float(self) % other

    def __rmod__(self, other):
        return other % float(self)

    def __pow__(self, power, modulo=None):
        self.is_numeric(power)
        return float(self) ** power

    def __rpow__(self, other):
        other = self.is_numeric(other)
        return other ** float(self)

    def __iadd__(self, other):
        if isinstance(other, RandomFloat):
            return RandomFloat(self.mu + other)
        elif not isinstance(other, float):
            raise TypeError
        return RandomFloat(self.mu + other)

    def __lt__(self, other):
        other = self.is_numeric(other)
        return float(self) < other

    def __le__(self, other):
        other = self.is_numeric(other)
        return float(self) <= other

    def __gt__(self, other):
        other = self.is_numeric(other)
        return float(self) > other

    def __ge__(self, other):
        other = self.is_numeric(other)
        return float(self) >= other