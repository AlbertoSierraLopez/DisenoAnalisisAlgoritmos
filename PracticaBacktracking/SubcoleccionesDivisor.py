def subcolecciones_principal(coleccion, n, m):
    soluciones = [None] * n
    subcolecciones(0, coleccion, m, soluciones, 0)


# i:            indice de la iteración
# coleccion:    vector de números
# m:            tamaño de la subcolección
# soluciones:   vector de boolenos que representa la subcolección
# s:            número de subcolecciones de tamaño m
def subcolecciones(i, coleccion, m, soluciones, s):
    # Caso Base: sub-colección completa
    if i == n:
        divisores = recortar(coleccion, soluciones)
        if len(divisores) == m and es_divisor(divisores[0], divisores[1:]):
            s = s + 1
    else:
        return 0


# Devuelve una lista con los elementos de coleccion que estaban a True en solucion
# El primero de la lista deve ser divisor de los otros m-1 elementos
def recortar(coleccion, soluciones):
    if soluciones == [] and coleccion == []:
        return []
    else:
        if soluciones[0] == True:
            return [coleccion[0]] + recortar(coleccion[1:], soluciones[1:])
        else:
            return recortar(coleccion[1:], soluciones[1:])


# Comprueba si el divisor es divisor de todos los números de la lista dividendos
def es_divisor(divisor, dividendos):
    if dividendos == []:
        return True
    else:
        return (dividendos[0] % divisor == 0) and es_divisor(divisor, dividendos[1:])


n = 5
coleccion = [2, 2, 5, 4, 7]
soluciones = [0, 1, 0, 1, 0]
m = 2

divisores = recortar(coleccion, soluciones)
print(es_divisor(divisores[0], divisores[1:]))
