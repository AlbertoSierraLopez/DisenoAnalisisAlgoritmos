def Elemento_Mayoritario(a):
    n = len(a)
    if n == 1:
        return (True, a[0], 1)
    else:
        n2 = n // 2
        t1 = Elemento_Mayoritario(a[:n2])
        t2 = Elemento_Mayoritario(a[n2:])
        if t1[0]:
            p = Contar_Apariciones(a[n2:], t1[1])
            p += t1[2]
            if p > n2:
                return (True, t1[1], p)
        if t2[0]:
            q = Contar_Apariciones(a[:n2], t2[1])
            q += t2[2]
            if q > n2:
                return (True, t2[1], q)
        return (False, None, 0)


def Contar_Apariciones(a, e):
    if a == []:
        return 0
    elif a[0] == e:
        return 1 + Contar_Apariciones(a[1:], e)
    else:
        return Contar_Apariciones(a[1:], e)


a = [4, 4, 5, 4, 1, 5, 4, 3, 4]
print(Elemento_Mayoritario(a))
