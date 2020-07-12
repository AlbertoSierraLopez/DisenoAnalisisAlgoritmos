def suma_lenta(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        return suma_lenta(a - 1, b - 1) + 2


x = int(input())
y = int(input())
print(suma_lenta(x, y))
