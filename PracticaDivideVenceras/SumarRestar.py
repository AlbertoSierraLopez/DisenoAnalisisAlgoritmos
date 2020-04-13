def suma_polinomios(polinomio_1, polinomio_2):
    n_1 = len(polinomio_1) - 1
    n_2 = len(polinomio_2) - 1
    if n_1 < 0:
        return polinomio_2
    elif n_2 < 0:
        return polinomio_1
    else:
        if n_1 > n_2:
            return suma_polinomios(polinomio_1[0:n_1], polinomio_2) + [polinomio_1[n_1]]
        elif n_2 > n_1:
            return suma_polinomios(polinomio_1, polinomio_2[0:n_2]) + [polinomio_2[n_2]]
        else:
            return suma_polinomios(polinomio_1[0:n_1], polinomio_2[0:n_2]) + [polinomio_1[n_1] + polinomio_2[n_2]]


def resta_polinomios(polinomio_1, polinomio_2):
    n_1 = len(polinomio_1) - 1
    n_2 = len(polinomio_2) - 1
    if n_1 < 0:
        return polinomio_2
    elif n_2  < 0:
        return polinomio_1
    else:
        if n_1 > n_2:
            return resta_polinomios(polinomio_1[0:n_1], polinomio_2) + [polinomio_1[n_1]]
        elif n_2 > n_1:
            return resta_polinomios(polinomio_1, polinomio_2[0:n_2]) + [- polinomio_2[n_2]]
        else:
            return resta_polinomios(polinomio_1[0:n_1], polinomio_2[0:n_2]) + [polinomio_1[n_1] - polinomio_2[n_2]]


#################################################


def imprimir_polinomio(a, g):   # g representa la iteración, empieza en 0
    n = len(a)
    # Si en la primera iteración el último elemento de la lista es 0, el polinomio será la constante 0
    if g == 0 and a[n - 1] == 0:  # g = n-1 = 0
        print(" + 0", sep='')
    else:
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
            imprimir_polinomio(a[0:n - 1], g + 1)


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


grado_1 = int(input())
polinomio_1 = lee_lista(grado_1 + 1)
grado_2 = int(input())
polinomio_2 = lee_lista(grado_2 + 1)
imprimir_polinomio(suma_polinomios(polinomio_1, polinomio_2), 0)
imprimir_polinomio(resta_polinomios(polinomio_1, polinomio_2), 0)
