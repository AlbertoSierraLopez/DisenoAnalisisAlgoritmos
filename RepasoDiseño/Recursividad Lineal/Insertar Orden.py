def Insertar_Orden(a, n):
    k = len(a)
    if k == 0:
        return [n]
    elif n <= a[0]:
        return [n] + a
    else:
        return [a[0]] + Insertar_Orden(a[1:], n)


a = [2, 4, 6, 8]
n = int(input())
print(a)
print(Insertar_Orden(a, n))
