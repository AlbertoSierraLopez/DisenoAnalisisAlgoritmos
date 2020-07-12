def suma_digitos(n):
    if n < 10:
        return n
    else:
        return suma_digitos(n // 10) + n % 10


x = int(input())
print(suma_digitos(x))
