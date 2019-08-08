from Interpolacion import*
import pylab as pl
x = [2,4,5]
y = [5,6,3]
p = lagrange(x,y)
print(p)
print()
r = lagrange(x,y,4.25)
print(r)
print()
r = lagrange(x,y,[3.15,3.74,4.25])
print(r)