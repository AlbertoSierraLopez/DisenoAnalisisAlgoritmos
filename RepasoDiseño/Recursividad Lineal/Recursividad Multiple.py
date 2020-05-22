def f_Iterativa(n):
    if n == 1 or n == 2:
        return 1
    else:
        acc = 1
        for i in range(1, n-1):
            acc += f_Iterativa(i)
        return acc

def f_Recursiva(n):
    if n == 1 or n == 2:
        return 1
    else:
        return 1 + sumatorio(n-2)


def sumatorio(n):
    if n == 1:
        return f_Recursiva(n)
    else:
        return f_Recursiva(n) + sumatorio(n - 1)


n = int(input())
print("Iterativa:", f_Iterativa(n))
print("Recursiva:", f_Recursiva(n))
