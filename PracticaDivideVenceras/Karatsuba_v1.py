def karatsuba(polinomio_1, polinomio_2):
    grado_1 = len(polinomio_1) - 1
    grado_2 = len(polinomio_2) - 1
    m = min(len(polinomio_1) // 2, len(polinomio_2) // 2)

    # Caso Base
    # Cuando uno de los polinomios tiene grado 0 basta con multiplicar esa constante por cada uno de los coeficientes del otro polinomio
    # Está implementado como un map que multiplica una constante por una lista
    # También se podría hacer utilizando suma_polinomios() para sumar el polinomio consigo mismo
    # tantas veces como la constante (el polinomio de longitud 1), pero conlleva más operaciones
    if grado_1 == 0:
        return list(map(lambda x: x * polinomio_1[0], polinomio_2))
    elif grado_2 == 0:
        return list(map(lambda x: x * polinomio_2[0], polinomio_1))

    # Caso Recursivo
    else:
        a = polinomio_1[m:]
        b = polinomio_1[:m]
        c = polinomio_2[m:]
        d = polinomio_2[:m]

        ac = karatsuba(a, c)
        bd = karatsuba(b, d)
        t = resta_polinomios(resta_polinomios(karatsuba(suma_polinomios(a, b), suma_polinomios(c, d)), ac), bd)

        return suma_polinomios(suma_polinomios(desplazar_izq(ac, m * 2), desplazar_izq(t, m)), bd)


# Los desplazamientos están al revés porque la lista polinomio está al REVÉS (izq <-> der)
# Desplazar a la izquierda el polinomio es meter 0's por el principio de la lista
def desplazar_izq(a, n):
    if n == 0:
        return a
    else:
        return [0] + desplazar_izq(a, n - 1)


#################################################


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
    elif n_2 < 0:
        return polinomio_1
    else:
        if n_1 > n_2:
            return resta_polinomios(polinomio_1[0:n_1], polinomio_2) + [polinomio_1[n_1]]
        elif n_2 > n_1:
            return resta_polinomios(polinomio_1, polinomio_2[0:n_2]) + [- polinomio_2[n_2]]
        else:
            return resta_polinomios(polinomio_1[0:n_1], polinomio_2[0:n_2]) + [polinomio_1[n_1] - polinomio_2[n_2]]


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
producto = karatsuba(polinomio_1, polinomio_2)
imprimir(producto)
