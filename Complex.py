class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def __str__(self):
        if self.img > 0:
            sgn = "+"
        else:
            sgn = ''
        return str(self.real) + sgn + str(self.img)+"j"

    def add(self, n2):
        return Complex(self.real+n2.real , self.img+n2.img)

    def mul(self, n2):
        r1 = (self.real)*(n2.real) - (self.img)*(n2.img)
        i1 = (self.real)*(n2.img) + (self.img)*(n2.real)
        return Complex(r1, i1)

    def conj(self):
        return Complex(self.real, (self.img)*-1)

    def div(self, n2):
        num = self.mul(n2.conj())
        den = (n2.real)**2 + (n2.img)**2

        r1 = num.real / den
        i1 = num.img / den

        return Complex(r1, i1)


n1 = Complex(5,-6)
n2 = Complex(7, 8)

print("n1 = ",n1)
print("n2 = ", n2)

x = n1.mul(n2)
x = n1.add(n2)

print("Multiplied :", x)

y = n1.div(n2)
print("Divided: ", y)

