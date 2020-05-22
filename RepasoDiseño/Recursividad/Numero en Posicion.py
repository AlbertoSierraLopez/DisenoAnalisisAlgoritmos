# Ejercicio 5. 7
def Numero_en_Posicion(a, lower, upper):
    middle = (lower + upper) // 2
    if lower > upper:
        return -1
    elif a[middle] == middle:
        return middle
    elif a[middle] > middle:
        return Numero_en_Posicion(a, lower, middle - 1)
    else:
        return Numero_en_Posicion(a, middle + 1, upper)


a = [-3, -1, 2, 5, 6, 7, 9]
print(Numero_en_Posicion(a, 0, len(a) - 1))