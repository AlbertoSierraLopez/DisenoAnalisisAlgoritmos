def Insertar_Digito(a, x):
    if a == 0:
        return x
    elif x >= a % 10:
        return a * 10 + x
    else:
        return Insertar_Digito(a // 10, x) * 10 + a % 10


a = 245778
x = int(input())
print(Insertar_Digito(a, x))
