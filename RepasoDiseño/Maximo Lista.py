def Maximo_Lista(a):
    k = len(a)
    if k == 1:
        return a[0]
    else:
        return max(a[k - 1], Maximo_Lista(a[:k - 1]))


a = [1, 2, 9, 5, 2, 8, 3, 5, 2]
print(Maximo_Lista(a))