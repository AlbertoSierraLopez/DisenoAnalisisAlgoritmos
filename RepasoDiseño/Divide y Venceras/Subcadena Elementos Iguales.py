# Ejercicio 7.6
def Es_Subcadena_Elementos_Iguales(a):
    k = len(a)
    if k <= 1:
        return True
    else:
        return a[0] == a[1] and Es_Subcadena_Elementos_Iguales(a[1:])

def Subcadena_Elementos_Iguales_Mas_Larga(a):
    if Es_Subcadena_Elementos_Iguales(a):
        return a
    else:
        a1 = Subcadena_Elementos_Iguales_Mas_Larga(a[:len(a) - 1])
        a2 = Subcadena_Elementos_Iguales_Mas_Larga(a[1:])
        if len(a1) > len(a2):
            return a1
        else:
            return a2


def Subcadena_Elementos_Iguales_Mas_Larga_ALT(a):
    k = len(a)
    if k <= 1:
        return a
    else:
        aux = Subcadena_Elementos_Iguales_Mas_Larga_ALT(a[1:])
        if len(aux) == k - 1 and a[0] == aux[0]:
            return a
        else:
            a1 = Subcadena_Elementos_Iguales_Mas_Larga_ALT(a[:len(a) - 1])
            a2 = Subcadena_Elementos_Iguales_Mas_Larga_ALT(a[1:])
            if len(a1) > len(a2):
                return a1
            else:
                return a2


a = [1, 3, 5, 5, 4, 4, 4, 5, 5, 6]
print(Subcadena_Elementos_Iguales_Mas_Larga(a))
print(Subcadena_Elementos_Iguales_Mas_Larga_ALT(a))
