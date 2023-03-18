from math import atan, atan2


class Complex:

    def __init__(self, re: float, im: float):
        self.re = re
        self.im = im

    def __str__(self):
        return f'{self.re:0.4f} + {self.im:0.4f}i'

    def __repr__(self):
        return f'Complex(re={self.re}, im={self.im})'

    def __add__(self, other: 'Complex') -> 'Complex':
        return Complex(self.re + other.re,
                       self.im + other.im)

    def __sub__(self, other: 'Complex') -> 'Complex':
        return Complex(self.re - other.re,
                       self.im - other.im)

    def __neg__(self) -> 'Complex':
        return Complex(-self.re, -self.im)

    def __mul__(self, other: 'Complex') -> 'Complex':
        return Complex(self.re * other.re - self.im * other.im,
                       self.re * other.im + self.im * other.re)

    def __abs__(self) -> float:
        return (self.re * self.re + self.im * self.im) ** 0.5

    def exponential(self) -> str:
        phi = atan2(self.im, self.re)
        return f'{abs(self)}*e^i*{phi:0.4f}'

    def polar(self) -> str:
        phi = atan2(self.im, self.re)
        return f'{abs(self)}*(sin({phi:0.4f}) + i*cos({phi:0.4f}))'


class False_complex(Complex):
    def __mul__(self, other: 'False_complex') -> 'False_complex':
        return False_complex(self.re * other.re,
                             self.im * other.im)


class Trianion(Complex):
    def __init__(self, re: float, im: float, jim: float):
        super().__init__(re, im)
        self.jim = jim

    def __add__(self, other: 'Trianion') -> 'Trianion':
        return Trianion(self.re + other.re, self.im + other.im,
                        self.jim + other.jim)

    def __sub__(self, other: 'Trianion') -> 'Trianion':
        return Trianion(self.re - other.re, self.im - other.im,
                        self.jim - other.jim)

    def __mul__(self, other: 'Trianion') -> 'Trianion':
        return Trianion(self.re * other.re - self.im * other.im - self.jim * other.im -
                        self.im * other.jim - self.jim * other.jim,
                        self.im * other.re + self.re * other.im,
                        self.jim * other.re + self.re * other.jim)

    def __str__(self):
        return f'{self.re:0.4f} + {self.im:0.4f}i + {self.jim:0.4f}j'


class Bicomplex:
    def __init__(self, num1: Complex, num2: Complex):
        self.comp1 = num1
        self.comp2 = num2

    def __add__(self, other: 'Bicomplex') -> 'Bicomplex':
        return Bicomplex(self.comp1 + other.comp1, self.comp2 + other.comp2)

    def __sub__(self, other: 'Bicomplex') -> 'Bicomplex':
        return Bicomplex(self.comp1 - other.comp1, self.comp2 - other.comp2)

    def __str__(self):
        return f'{self.comp1}\n{self.comp2}'

    def __mul__(self, other: 'Bicomplex') -> 'Bicomplex':
        return Bicomplex(self.comp1 * other.comp1, self.comp2 * other.comp2)


# a = Complex(4.12345, 0.987654)
# print(a)
# print(repr(a))
# b = eval(repr(a))
# print(b)
# print(repr(b))
# # print(exec('print(10*5)'))
# print(eval('print(10*5)'))
# print(hash(a) == hash(b))
# c = a
# print(hash(a) == hash(c))
# print(a + b)
# d = Complex(0, 1)
# print(Complex.exponential(d))
# print(Complex.polar(d))
#
# a = False_complex(1, 1)
# b = False_complex(2, 2)
#
# print(a * b)

bi = Bicomplex(Complex(1, 1), Complex(1, 1))
ai = Bicomplex(Complex(2, 2), Complex(2, 2))
print(ai + bi)
print(ai - bi)
