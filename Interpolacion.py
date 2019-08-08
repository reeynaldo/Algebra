from sympy import*
def lagrange(x,y, u = None):
    n = len(x)
    t = Symbol('t')
    p = 0
    for i in range(n):
        L = 1
        for j in range(n):
            if j != i:
                L = L * (t -x[j]) / (x[i] -x[j])
        p = p + y[i] * L
        p = expand(p)
    if u == None:
        return p
    elif type(u) == list:
        v = []
        for i in range(len(u)):
            v = v + [p.subs(t,u[i])]
        return v
    else:
        return p.subs(t,u)