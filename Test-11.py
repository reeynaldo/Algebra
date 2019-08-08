from Interpolacion import*
import pylab as pl

x = [2,4,5]
y = [5,6,3]
u = pl.arange(2,5.1,0.1)
v = lagrange(x,y, list(u))
pl.plot(u,v)
pl.plot(x,y,'o')
pl.grid(True)
pl.show()