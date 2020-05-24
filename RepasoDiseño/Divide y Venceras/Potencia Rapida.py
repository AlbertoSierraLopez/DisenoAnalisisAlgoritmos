def Potencia(b, e):
    if e == 0:
        return 1
    else:
        if even(e):
            p = Potencia(b, e // 2)
            return p ** 2
        else:
            p = Potencia(b, (e - 1) // 2)
            return b * p ** 2


def even(n):
    return n % 2 == 0


print("Base:")
b = int(input())
print("Exponente:")
e = int(input())
print(Potencia(b, e))
