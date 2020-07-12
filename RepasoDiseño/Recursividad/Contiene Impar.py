# Ejercicio 5.1
def Contiene_Impar(n):
    if n < 10:
        return n % 2 == 1
    elif (n % 10) % 2 == 1:
        return True
    else:
        return Contiene_Impar(n // 10)


n = int(input())
print(Contiene_Impar(n))
