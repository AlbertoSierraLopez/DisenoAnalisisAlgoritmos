# Out of place
def Mergesort(a):
    k = len(a)
    if k == 1:
        return a
    else:
        m = k // 2
        a1 = Mergesort(a[:m])
        a2 = Mergesort(a[m:])
        return Merge(a1, a2)


def Merge(a1, a2):
    if a1 == []:
        return a2
    elif a2 == []:
        return a1
    else:
        if a1[0] < a2[0]:
            return [a1[0]] + Merge(a1[1:], a2)
        else:
            return [a2[0]] + Merge(a1, a2[1:])


a = [7, 3, 4, 8, 1, 4, 6, 4]
print(Mergesort(a))
print(a)
