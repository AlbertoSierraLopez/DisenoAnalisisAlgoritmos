def num_posicion(a):
    if len(a) == 0:
        return -1
    if len(a) - 1 == a[len(a) - 1]:
        return a[len(a) - 1]
    else:
        return num_posicion(a[0:len(a) - 1])


def num_posicion_divide(a, ini, fin):
    mitad = (fin + ini + 1) // 2
    if ini > fin:
        return -1
    if a[mitad] == mitad:
        return mitad
    else:
        if mitad < a[mitad]:
            return num_posicion_divide(a, ini, mitad - 1)
        else:
            return num_posicion_divide(a, mitad, fin)


lista = []
print(lista)
print(num_posicion(lista))
print(num_posicion_divide(lista, 0, len(lista) - 1))
