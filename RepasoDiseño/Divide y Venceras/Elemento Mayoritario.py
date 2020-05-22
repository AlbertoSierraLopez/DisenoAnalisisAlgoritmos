def Mayoritario(a):
    if a == []:
        return (False, None, 0)
    elif len(a) == 1:
        return (True, a[0], 1)
    else:
        m = len(a) // 2
        a1 = Mayoritario(a[:m])
        a2 = Mayoritario(a[m:])

        if a1[0]:
            n = a1[2] + Contar_Apariciones(a[m:], a1[1])
            if n > m:
                return (True, a1[1], n)

        elif a2[0]:
            n = a2[2] + Contar_Apariciones(a[:m], a2[1])
            if n > m:
                return (True, a2[1], n)

        return (False, None, 0)


def Contar_Apariciones(a, e):
    if a == []:
        return 0
    elif a[0] == e:
        return 1 + Contar_Apariciones(a[1:], e)
    else:
        return Contar_Apariciones(a[1:], e)


a = [4, 4, 5, 4, 1, 2, 4, 3]
print(Mayoritario(a))
