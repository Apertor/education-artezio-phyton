class Complex(complex):
    re = 0.0
    im = 0.0

    def __init__(self, re, im):
        self.re = re
        self.im = im

    def __add__(self, other):
        return Complex(self.re + other.re, self.im + other.im)

    def __sub__(self, other):
        return Complex(self.re - other.re, self.im - other.im)

    def __mul__(self, other):
        res = super(Complex, self).__mul__(other)
        return Complex(res.real, res.imag)

    def __truediv__(self, other):
        res = super(Complex, self).__truediv__(other)
        return Complex(res.real, res.imag)

    def __abs__(self):
        rel = (self.re**2 + self.im**2)**0.5
        return Complex(rel, 0)

    def __str__(self):
        sign = ''
        if self.im >= 0:
            sign = '+'
        return '{}{}{}i'.format("%.2f" %(self.re), sign, "%.2f" %(self.im))

comp1 = Complex(2, 1)
comp2 = Complex(5, 6)

# print(comp1)
# print(comp2)
print(comp1+comp2)
print(comp1-comp2)
print(comp1*comp2)
print(comp1/comp2)
print(comp1.__abs__())
print(comp2.__abs__())
