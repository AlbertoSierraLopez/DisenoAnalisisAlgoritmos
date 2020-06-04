def evaluar_polinomio(P, x):
    n = len(P)                  # n - 1 es el grado, n es la longitud de la lista P
    # if n == 0:                # Caso base redundante
    #     return 0
    if n == 1:
        return P[0]
    else:
        division = dividir_wrapper(P)
        pares = division[0]
        impares = division[1]
        return evaluar_polinomio(pares, x * x) + x * evaluar_polinomio(impares, x * x)


###################
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
###################

P = [1, 2, 3, 4, 5]
x = int(input())
print(evaluar_polinomio(P, x))
