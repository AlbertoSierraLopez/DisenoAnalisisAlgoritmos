def Busqueda_Binaria(a, n):
    if a == []:
        return -1
    else:
        i = len(a) // 2
        if a[i] == n:
            return i
        elif a[i] > n:
            return Busqueda_Binaria(a[:i], n)
        else:
            return i + 1 + Busqueda_Binaria(a[i + 1:], n)


a = [1, 3, 5, 7, 9, 11, 13, 15]
n = int(input())
print(Busqueda_Binaria(a, n))
