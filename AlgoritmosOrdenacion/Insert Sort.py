def Insert_Sort(a, i):
    k = len(a)
    if i == k:
        return a
    else:
        return Insert_Sort(Insertar_Orden(a[:i], a[i]) + a[i + 1:], i + 1)


def Insertar_Orden(a, n):
    k = len(a)
    if k == 0:
        return [n]
    elif n <= a[0]:
        return [n] + a
    else:
        return [a[0]] + Insertar_Orden(a[1:], n)


a = [7, 3, 4, 9, 1, 2, 6, 8, 5]
print(a)
print(Insert_Sort(a, 0))
