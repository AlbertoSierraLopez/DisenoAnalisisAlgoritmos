def Triangulo_Pascal(n):
    if n == 1:
        return [1]
    else:
        return [1] + aux(Triangulo_Pascal(n - 1)) + [1]


def aux(a):
    if len(a) == 1:
        return []
    else:
        return [a[0] + a[1]] + aux(a[1:])


n = int(input())
for i in range(1, n + 1):
    print(Triangulo_Pascal(i))
