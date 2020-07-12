def suma_impares(n):
    if n == 1:
        return (2 * n - 1)
    else:
        return (2 * n - 1) + suma_impares(n - 1)


x = int(input())
print(suma_impares(x))
