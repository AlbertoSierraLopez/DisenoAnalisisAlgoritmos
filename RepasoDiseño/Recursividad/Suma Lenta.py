def Suma_Lenta(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        return 2 + Suma_Lenta(a - 1, b - 1)


a = int(input())
b = int(input())
print(Suma_Lenta(a, b))
