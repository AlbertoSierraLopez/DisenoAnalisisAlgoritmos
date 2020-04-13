def imprimir(n):
    if n < 10:
        print(n)
    else:
        imprimir(n // 10)
        print(n % 10)


def imprimir_reves(n):
    if n < 10:
        print(n)
    else:
        print(n % 10)
        imprimir_reves(n // 10)


x = int(input())
imprimir(x)
print("---oooo---")
imprimir_reves(x)
