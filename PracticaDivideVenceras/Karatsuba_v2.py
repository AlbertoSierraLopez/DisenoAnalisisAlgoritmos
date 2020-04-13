def karatsuba(polinomio_1, polinomio_2):
    grado_1 = len(polinomio_1) - 1
    grado_2 = len(polinomio_2) - 1
    desplazamiento = 0

    # Esta condición sirve para igualar la longitud de los polinomios con ceros por la izquierda (por la derecha en la lista)
    # Las posiciones desplazadas se almacenan y se deshacen en el polinomio final (es necesario por cómo está implementado imprimir_polinomio())
    if grado_1 != grado_2:
        if grado_1 > grado_2:
            desplazamiento = grado_1 - grado_2
            polinomio_2 = desplazar_der(polinomio_2, grado_1 - grado_2)
        else:
            desplazamiento = grado_2 - grado_1
            polinomio_1 = desplazar_der(polinomio_1, desplazamiento)

    # La m siempre debe ser mayor que 0 para evitar bucles infinitos
    m = min(len(polinomio_1) // 2, len(polinomio_2) // 2)

    # Caso Base
    if grado_1 == 0 and grado_2 == 0:
        return [polinomio_1[0] * polinomio_2[0]]
    elif grado_1 < 0:
        return polinomio_2
    elif grado_2 < 0:
        return polinomio_1

    # Caso Recursivo
    else:
        a = polinomio_1[m:]
        b = polinomio_1[:m]
        c = polinomio_2[m:]
        d = polinomio_2[:m]

        ac = karatsuba(a, c)
        bd = karatsuba(b, d)
        t = resta_polinomios(resta_polinomios(karatsuba(suma_polinomios(a, b), suma_polinomios(c, d)), ac), bd)

        retorno = suma_polinomios(suma_polinomios(desplazar_izq(ac, m * 2), desplazar_izq(t, m)), bd)
        return retorno[:len(retorno) - desplazamiento]


# Los desplazamientos están al revés porque la lista polinomio está al REVÉS (izq <-> der)
# Desplazar a la izquierda el polinomio es meter 0's por el principio de la lista
def desplazar_izq(a, n):
    if n == 0:
        return a
    else:
        return [0] + desplazar_izq(a, n - 1)


def desplazar_der(a, n):
    if n == 0:
        return a
    else:
        return desplazar_der(a, n - 1) + [0]


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


def imprimir_polinomio(a, it):   # it representa la iteración, empieza en 0
    n = len(a)
    # Si en la primera iteración el último elemento de la lista es 0, el polinomio será la constante 0
    if it == 0 and a[n - 1] == 0:
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
            imprimir_polinomio(a[0:n - 1], it + 1)


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
imprimir_polinomio(producto, 0)
