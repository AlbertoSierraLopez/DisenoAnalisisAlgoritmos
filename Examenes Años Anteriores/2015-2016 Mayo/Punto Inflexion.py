def Punto_Inflexion(a, lower, upper):
    if lower > upper:
        return -1
    else:
        middle = (lower + upper) // 2
        if a[middle] % 2 == 0:
            next = Punto_Inflexion(a, middle + 1, upper)
            if next == -1:
                return middle
            else:
                return next
        else:
            return Punto_Inflexion(a, lower, middle - 1)


a = [2, -4, 10, 8, 0, 12, 9, 3, -15, 3, 1]
p = Punto_Inflexion(a, 0, len(a) - 1)
print(a[p], p)
