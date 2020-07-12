# Ejercicio 7.3
def Regla_Imperial(n, k):
    if n == 0:
        for i in range(k + 1):
            print("-", end='')
        print('', n)
    else:
        Regla_Imperial(n - 1, k)
        Separacion(k)
        for i in range(k + 1):
            print("-", end='')
        print('', n)


def Separacion(k):
    if k > 0:
        Separacion(k - 1)
        for i in range(k):
            print("-", end='')
        print()
        Separacion(k - 1)


n = int(input())
k = int(input())
Regla_Imperial(n, k)
