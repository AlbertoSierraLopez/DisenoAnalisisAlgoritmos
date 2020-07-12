def sumar(n):
    if n == 1:
        return 1
    else:
        return sumar(n - 1) + n


x = int(input())
print(sumar(x))
