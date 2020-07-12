def Horner(a, x):
    k = len(a)
    if k == 1:
        return a[0]
    else:
        return a[k-1] + x * Horner(a[:k-1], x)


a = [3, 2, 4, 1]
x = int(input())
print(Horner(a, x))
