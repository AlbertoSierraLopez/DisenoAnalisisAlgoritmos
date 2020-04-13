def numero_digitos(n):
    if n < 10:
        return 1
    else:
        return 1 + numero_digitos(n // 10)


x = int(input())
print(numero_digitos(x))
