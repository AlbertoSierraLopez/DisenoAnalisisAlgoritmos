# Suma los n primeros números impares
def Suma_Impares(n):
    if n == 1:
        return 1
    else:
        return 2 * n - 1 + Suma_Impares(n - 1)


n = int(input())
print(Suma_Impares(n))
