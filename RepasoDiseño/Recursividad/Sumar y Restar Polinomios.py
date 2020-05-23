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
    if gq == 0:
        return p
    elif gp == 0:
        return Restar_Polinomios(p, q[:gq - 1]) + [- q[gq - 1]]

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
print("a:")
Imprimir_Polinomio(a, len(a) - 1)

b = [2, 1, 4, 9, 1]
print("b:")
Imprimir_Polinomio(b, len(b) - 1)

print("Suma:")
suma = Sumar_Polinomios(a, b)
Imprimir_Polinomio(suma, len(suma) - 1)

print("Resta:")
resta = Restar_Polinomios(a, b)
Imprimir_Polinomio(resta, len(resta) - 1)
