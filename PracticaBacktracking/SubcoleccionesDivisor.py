def subcolecciones_principal(coleccion, n, m):
    soluciones = [None] * n
    s = 0
    subcolecciones(0, coleccion, n, m, soluciones, s)
    print(s)


# i:            indice de la iteración
# coleccion:    vector de números
# m:            tamaño del vector de numeros
# m:            tamaño de la subcolección
# soluciones:   vector de boolenos que representa la subcolección
# s:            número de subcolecciones de tamaño m que cumplen las restricciones
def subcolecciones(i, coleccion, n, m, soluciones, s):
    # Caso Base: sub-colección completa
    # Si la sub-coleccion tiene m elementos y el primero de ellos es el divisor de los demás, he encontrado una solución
    # Como no es necesario mostrar la solución, simplemente sumo uno a la variable s
    if i == n:
        divisores = __recortar(coleccion, soluciones)
        if len(divisores) == m and __es_divisor(divisores[0], divisores[1:]):
            s = s + 1
    else:
        for k in range(0, 2):
            # Ramificación en el arbol, se inserta o no el candidato coleccion[i] en la solucion parcial
            soluciones[i] = k

            # Se expande la solucion
            subcolecciones(i + 1, coleccion, n, m, soluciones, s)

            # Se deshace el candidato
            soluciones[i] = None


# Devuelve una lista con los elementos de coleccion que estaban a True en solucion
# El primero de la lista deve ser divisor de los otros m-1 elementos
def __recortar(coleccion, soluciones):
    if soluciones == [] and coleccion == []:
        return []
    else:
        if soluciones[0]:
            return [coleccion[0]] + __recortar(coleccion[1:], soluciones[1:])
        else:
            return __recortar(coleccion[1:], soluciones[1:])


# Comprueba si el divisor es divisor de todos los números de la lista dividendos
def __es_divisor(divisor, dividendos):
    if dividendos == []:
        return True
    else:
        return (dividendos[0] % divisor == 0) and __es_divisor(divisor, dividendos[1:])


n = 5
coleccion = [2, 2, 5, 4, 7]
m = 2

"""
soluciones = [0, 1, 0, 1, 0]
divisores = recortar(coleccion, soluciones)
print(es_divisor(divisores[0], divisores[1:]))
"""

subcolecciones_principal(coleccion, n, m)