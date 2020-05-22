# Ejercicio 5.8
# Devuelve el mayor indice de la lista que contiene un numero par suponinedo que la lista tiene primero los números pares y luego los impares
def Mayor_Numero_Par(a, lower, upper):
    middle = (lower + upper) // 2
    if lower > upper:
        return - 1
    else:
        if odd(a[middle]):
            return Mayor_Numero_Par(a, lower, middle - 1)
        else:
            next = Mayor_Numero_Par(a, middle + 1, upper)
            if next != -1:
                return next
            else:
                return middle


def even(n):
    return n % 2 == 0


def odd(n):
    return n % 2 == 1


a = [2, -4, 10, 8, 2, 6, 9, 3, 1]
print(Mayor_Numero_Par(a, 0, len(a) - 1))
