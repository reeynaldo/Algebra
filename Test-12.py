from Lineal import*

def g(t): return -7*t**2/6 + 15*t/2 - 28/3
s = biseccion(g,4,5,0.0001)
print(s)