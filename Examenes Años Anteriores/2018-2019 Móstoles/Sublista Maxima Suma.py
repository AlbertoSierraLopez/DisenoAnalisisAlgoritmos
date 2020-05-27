import math

def Sublista_Maxima_Suma(a):
    n = len(a)

    if n == 1:
        return a
    else:
        s1 = Sublista_Maxima_Suma(a[1:])
        s2 = Sublista_Maxima_Suma(a[:n - 1])
        return Maxima_Lista(a, s1, s2)


def Maxima_Lista(a, b, c):
    sa = Suma(a)
    sb = Suma(b)
    sc = Suma(c)

    if sa >= sb and sa >= sc:
        return a
    elif sb >= sc:
        return b
    else:
        return c


def Suma(a):
    sum = 0
    for i in range(len(a)):
        sum += a[i]
    return sum


# Solución Manuel
def maxima_suma_sublista(a):
    n = len(a)
    if n==1:
        return a[0]
    else:
        mitad = n//2
        max_mitad_izq = maxima_suma_sublista(a[0:mitad])
        max_mitad_dcha = maxima_suma_sublista(a[mitad:])

        max_izq = -math.inf
        aux_suma = 0
        for i in range(mitad - 1, -1, -1):
            aux_suma = aux_suma + a[i]
            max_izq = max(max_izq, aux_suma)

        max_dcha = -math.inf
        aux_suma = 0
        for i in range(mitad, n):
            aux_suma = aux_suma + a[i]
            max_dcha = max(max_dcha, aux_suma)

    return max(max_mitad_izq, max_mitad_dcha, max_izq + max_dcha)

a = [-1, -4, 5, 2, -3, 4, 2, -5]
print(maxima_suma_sublista(a))
