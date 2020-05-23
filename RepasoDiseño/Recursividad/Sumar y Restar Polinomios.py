def Sumar_Polinomios(p, q):
    gp = len(p)
    gq = len(q)
    if gp == 0:
        return q
    elif gq == 0:
        return p
    else:
        return Sumar_Polinomios(p[:gp - 1], q[:gq - 1]) + [p[gp - 1] + q[gq - 1]]


def Restar_Polinomios(p, q):
    gp = len(p)
    gq = len(q)
    if gp == 0:
        return q
    elif gq == 0:
        return p
    else:
        return Restar_Polinomios(p[:gp - 1], q[:gq - 1]) + [p[gp - 1] - q[gq - 1]]


def Imprimir_Polinomio(a, i):
    k = len(a)
    if k == 0:
        print("0")
    elif k == 1:
        print(a[0])
    else:
        if a[0] != 0:
            if i > 1:
                print(a[0], "x^", i, " +", end=' ', sep='')
            else:
                print(a[0], "x", " +", end=' ', sep='')
        Imprimir_Polinomio(a[1:], i - 1)


a = [3, 5, 0, 1]
Imprimir_Polinomio(a, len(a) - 1)
print("+")
b = [2, 1, 4, 9, 1]
Imprimir_Polinomio(b, len(b) - 1)
print("__________")
suma = Sumar_Polinomios(a, b)
Imprimir_Polinomio(suma, len(suma) - 1)
