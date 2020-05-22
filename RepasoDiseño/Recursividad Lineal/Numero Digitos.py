def Numero_Digitos(n):
    if n < 10:
        return 1
    else:
        return 1 + Numero_Digitos(n // 10)


n = int(input())
print(Numero_Digitos(n))
