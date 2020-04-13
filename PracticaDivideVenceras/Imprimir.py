def imprimir(a):
    n = len(a)
    # Si en la primera iteración el último elemento de la lista es 0, el polinomio será la constante 0
    if a[n - 1] == 0:
        print(" + 0", sep='')
    else:
        __imprimir_polinomio(a)


def __imprimir_polinomio(a):
    n = len(a)
    if n == 1:
        if a[n - 1] == 0:
            print()
        elif a[n - 1] > 0:
            print(" + ", abs(a[0]), sep='')
        else:
            print(" - ", abs(a[0]), sep='')
    else:
        if a[n - 1] == 0:
            print(end='')
        elif a[n - 1] > 0:
            print(" + ", abs(a[n - 1]), "x^", n - 1, end='', sep='')
        else:
            print(" - ", abs(a[n - 1]), "x^", n - 1, end='', sep='')
        __imprimir_polinomio(a[0:n - 1])


#################################################


# Función iterativa para leer una lista de n números enteros
def lee_lista(n):
    a = []
    if n > 0:
        cadena_entrada = input()
        for i in range(0, n):
            elemento = int(cadena_entrada.split(" ")[i])
            a.append(elemento)
    return a


#################################################


grado = int(input())
polinomio = lee_lista(grado + 1)
imprimir(polinomio)
