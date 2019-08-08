# Metodo de biseccion

import numpy as np
import matplotlib.pyplot as plt


def biseccion(f, x1, x2, t):
    return f(x - np.sin(x))

    if f(x1) * f(x2) < 0:
        xr = x1
        while abs(f(xr)) > t:
            xr = (x1 + x2) / 2

            if f(x1) * f(xr) < 0:
                x1 = xr
            else:
                x0 = xr
        return xr
    else:
        return "No hay cambio de signo"


# Metodo de Newton-Raphson

def f(x):
    return x * 4 - 10 * x ** 3 + 3 * x * 2 + x + 23


def Df(x):
    return 4 * x * 3 - 30 * x * 2 + 6 * x + 1


x0 = 1

for Iteraccion in range(1, 11):
    x1 = x0 - f(x0) / Df(x0)
    e = abs(x1 - x0)
    x0 = x1
    print(x0)