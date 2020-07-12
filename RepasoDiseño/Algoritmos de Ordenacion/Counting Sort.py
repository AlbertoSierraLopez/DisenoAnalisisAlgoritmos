def Counting_Sort(a):
    n = len(a)
    m = max(a) + 1
    b = [0] * m
    for i in range(n):
        b[a[i]] += 1
    return Auxiliar(0, b)


def Auxiliar(n, b):
    if b == []:
        return []
    else:
        c = Auxiliar(n + 1, b[1:])
        for i in range(b[0]):
            c = [n] + c
        return c


a = [2, 2, 3, 2, 0, 1, 3, 2, 0, 0, 4]
print(a)
print(Counting_Sort(a))