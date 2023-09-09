class ComplexNumber:
    def __init__(self, number, real=0, imaginary=0):
        self.number = number
        self.real = real
        self.imaginary = imaginary
    def split_complex(self):
        delimiter = "+" if "+" in self.number else "-"
        real, imaginary = self.number.split(delimiter)
        return real, imaginary.rstrip('i')
    def __add__(self, other):
        real1, imag1 = self.split_complex()
        real2, imag2 = other.split_complex()
        real_sum = int(real1) + int(real2)
        imag_sum = int(imag1) + int(imag2)
        return ComplexNumber("", real_sum, imag_sum)
    def __str__(self):
        return f"{self.real} + {self.imaginary}i"
    def __sub__(self, other):
        real1, imag1 = self.split_complex()
        real2, imag2 = other.split_complex()
        real_dif = int(real1) - int(real2)
        imag_dif = int(imag1) - int(imag2)
        return ComplexNumber("", real_dif, imag_dif)
    def __mul__ (self, other):
        real1, imag1 = self.split_complex()
        real2, imag2 = other.split_complex()
        real_pro = int(real1) * int(real2)
        imag_pro = int(imag1) * int(imag2)
        return ComplexNumber("", real_pro, imag_pro)
    def __truediv__  (self, other):
        real1, imag1 = self.split_complex()
        real2, imag2 = other.split_complex()
        real_quo = float(real1) / float(real2)
        imag_quo = float(imag1) / float(imag2)
        return ComplexNumber("", real_quo, imag_quo)
    def __mod__  (self, other):
        real1, imag1 = self.split_complex()
        real2, imag2 = other.split_complex()
        real_mod = float(real1) % float(real2)
        imag_mod = float(imag1) % float(imag2)
        return ComplexNumber("", real_mod, imag_mod)
    def mod (self, other):
        real1, imag1 = self.split_complex()
        real2, imag2 = other.split_complex()
        real_mod = int(real2) % int(real1)
        imag_mod = int(imag2) % int(imag1)
        return ComplexNumber("", real_mod, imag_mod)
x = input("Enter the first complex number: ")
y = input("Enter the second complex number: ")
num1 = ComplexNumber(x)
num2 = ComplexNumber(y)
result_addition = num1+ num2
print(result_addition)
result_subtraction=num1-num2
print(result_subtraction)
result_multiplication=num1* num2
print(result_multiplication)
result_division=num1/num2
print(result_division)
result_mod12=num1%num2
print(result_mod12)
result_mod21=num2%num1
print(result_mod21)
