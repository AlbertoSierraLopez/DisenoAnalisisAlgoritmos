def dividir(a, i, par, impar):  # i es el índice que se considera en cada iteración, empieza en 0
    n = len(a)
    if i < n:                   # Cuando hemos recorrido todos los elementos de la lista, simplemente no hacemos nada
        if i % 2 == 0:
            par.append(a[i])
        else:
            impar.append(a[i])

        dividir(a, i + 1, par, impar)


def dividir_wrapper(a):         # Un posible envoltorio al que se le pasa la lista y devuelve una dupla con las dos listas de pares e impares
    par = []
    impar = []
    dividir(a, 0, par, impar)
    return (par, impar)


a = [3, 6, 5, 7, 0, 9, 2]
listas = dividir_wrapper(a)
print(listas[0], listas[1])
