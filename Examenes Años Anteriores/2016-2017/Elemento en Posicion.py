def Elemento_en_Posicion(a, lower, upper):
    if lower > upper:
        return -1
    else:
        middle = (lower + upper) // 2
        if a[middle] == middle:
            return middle
        elif a[middle] < middle:
            return Elemento_en_Posicion(a, middle + 1, upper)
        else:
            return Elemento_en_Posicion(a, lower, middle - 1)


a = [-3, -1, 0, 2, 4, 7, 10, 15]
print(Elemento_en_Posicion(a, 0, len(a) - 1))
