from Lineal import *
from numpy import *
a = array([[4, 2, 5], [2,5,8], [5, 4, 3]], float)
b = array([[60.7], [92.9], [56.30]], float)
print("Gauss 2:", gauss_jordan2(a,b))