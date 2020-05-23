# Ejercicio 6.2
def Digitos_Compartidos(a):
    k = len(a)
    if k == 0:
        return {}
    elif k == 1:
        return Digitos(a[0])
    else:
        a1 = Digitos_Compartidos(a[:k // 2])
        a2 = Digitos_Compartidos(a[k // 2:])
        return a1 & a2


def Digitos(n):
    if n < 10:
        return {n}
    else:
        s = Digitos(n // 10)
        s.add(n % 10)
        return s


a = [2348, 1349, 7523, 3215]
print(Digitos_Compartidos(a))
