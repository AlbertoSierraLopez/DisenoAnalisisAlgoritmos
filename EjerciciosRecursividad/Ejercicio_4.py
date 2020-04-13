def multiple_iterativo(n):
    if n == 1 or n == 2:
        return 1
    else:
        sumatorio = 0
        for i in range(1, n - 1):
            sumatorio += multiple_iterativo(i)
        return 1 + sumatorio


def multiple_recursivo(n):
    if n == 1 or n == 2:
        return 1
    else:
        return 1 + aux(n-2)


def aux(n):
    if n == 1:
        return multiple_recursivo(n)
    else:
        return aux(n-1) + multiple_recursivo(n)


x = int(input())
print("iterativo:", multiple_iterativo(x))
print("recursivo:", multiple_recursivo(x))
