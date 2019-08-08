from Lineal import*
x = [2,4,6]
f = [3.7,4.1,5.6]
r1 = lagrange(x,f,3)
f = [4.2,5.3,6.7]
r2 = lagrange(x,f,3)
f = [5.8,6.1,7.4]
r3 = lagrange(x,f,3)
f = [7.1,7.9,8.2]
r4 = lagrange(x,f,3)
y = [5,10,15,20]
f = [r1,r2,r3,r4]
p = lagrange(y,f,12)
print(p)