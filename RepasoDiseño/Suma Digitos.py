def Suma_Digitos(n):
    if n < 10:
        return n
    else:
        return n % 10 + Suma_Digitos(n // 10)

    
n = int(input())
print(Suma_Digitos(n))
