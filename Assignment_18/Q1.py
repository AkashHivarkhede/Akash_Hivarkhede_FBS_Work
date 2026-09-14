# Create a class Complex Number with data members as real and imag and add
# following methods :
# a. Constructor
# b. Destructor
# c. Overload +,- operator

class ComplexNumber:

    def __init__(self, real=0, imag=0):
        self.real = real
        self.imag = imag

    def __del__(self):
        print("Complex object destroyed")

    def __add__(self, other):
        real = self.real + other.real
        imag = self.imag + other.imag

        return ComplexNumber(real, imag)

    def __sub__(self, other):
        real = self.real - other.real
        imag = self.imag - other.imag

        return ComplexNumber(real, imag)

    def Display(self):
        print(self.real, "+", self.imag, "i")


c1 = ComplexNumber(10, 5)
c2 = ComplexNumber(4, 2)

c3 = c1 + c2

print("Addition:")
c3.Display()

c4 = c1 - c2

print("Subtraction:")
c4.Display()