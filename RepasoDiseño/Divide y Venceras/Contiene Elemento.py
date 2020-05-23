# Ejercicio 6.1
def Contiene_Elemento(a, x, lower, upper):
    if lower > upper:
        return False
    else:
        middle = (lower + upper) // 2
        if a[middle] != x:
            return Contiene_Elemento(a, x, lower, middle - 1) or Contiene_Elemento(a, x, middle + 1, upper)
        else:
            return True


a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
x = int(input())
print(Contiene_Elemento(a, x, 0, len(a) - 1))
