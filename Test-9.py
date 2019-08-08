from numpy import*
x=array([2,4,5], float)
f=array([5,6,3], float)
d=vander(x)
print(d)
c=linalg.cond(d,inf)
print(c)
a=linalg.solve(d,f)
print(a)