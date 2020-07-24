# Classes Definition & object calling....

# Method definiton in class & calling them

class Complex:
    def __init__(self,r=0.0,i=0.0):
        self._real = r
        self._imag = i
    def __add__(self,other):
        self._total_real = self._real + other._real
        self._total_imag = self._imag + other._imag
        return self._total_real,self._total_imag
    
    def __eq__(self,other):
        if self._real == other._real and self._imag == other._imag:
            return True
        else:
            return False
    def __sub__(self,other):
        self._sub_real = self._real - other._real
        self._sub_imag = self._imag - other._imag
        return self._sub_real,self._sub_imag
    def __mul__(self,other):
        self._mul_real = self._real*other._real-self._imag*other._imag
        self._mul_imag = self._imag*other._real+self._real*other._imag
        return self._mul_real,self._mul_imag

c1 = Complex(2,2)
c2 = Complex(-0.2,-0.1)
c3 = c1+c2
print('c3=',c3)

c4 = c1-c2
print(c4)

c5 = c1*c2
print(c5)



if c1 == c2:
    print('Attributes of c1 & c2 are same')
else:
    print('Attributes of c1 & c2 are NOT same')

if type(c1) == type(c3):
    print('c1 & c3 are of same type')
else:
    print('c1 & c3 are NOT same type')

if c1 is c3:
    print('c1 & c3 are pointing to same direction')
else:
    print('c1 & c3 are NOT pointing to same direction')
    
