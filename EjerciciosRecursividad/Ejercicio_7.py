def insert_sort(a):
    n = len(a)
    if n <= 1:
        return a
    else:
        return insertar_ordenada(insert_sort(a[0:n - 1]), a[n - 1])


def insertar_ordenada(a, x):
    n = len(a)
    if n == 0 or a[n - 1] <= x:
        return a + [x]
    else:
        return insertar_ordenada(a[0:n - 1], x) + [a[n - 1]]


def lee_lista(n):
    a = []
    if n > 0:
        cadenaEntrada = input()
        for i in range(0, n):
            elemento = int(cadenaEntrada.split(" ")[i])
            a.append(elemento)

    return a


def imprime_lista(a):
    n = len(a)
    if n == 0:
        pass
    elif n == 1:
        print(a[0])
    else:
        print(a[0], end='')
        print(' ', end='')
        imprime_lista(a[1:])


n = int(input())
lista = lee_lista(n)
imprime_lista(insert_sort(lista))
