def subcolecciones_principal(coleccion, n, m):
    subcoleccion = [0] * n
    s = [0]
    subcolecciones(0, coleccion, n, m, 0, subcoleccion, s)
    print(s[0])


# i:            indice de la iteración
# coleccion:    vector de números
# n:            tamaño del vector de numeros
# m:            tamaño de la subcolección
# ns:           número de elementos de la subcolección
# soluciones:   vector de boolenos que representa la subcolección
# s:            número de subcolecciones de tamaño m que cumplen las restricciones, está implementado
#               como una lista de un número porque de esta forma se puede modificar el valor desde la llamada recursiva
def subcolecciones(i, coleccion, n, m, ns, subcoleccion, s):
    # Caso Base: sub-colección completa
    # Si la sub-coleccion tiene m elementos y el menor de ellos es el divisor de los demás, he encontrado una solución
    # Como no es necesario mostrar la solución, simplemente sumo uno a la variable s
    if ns == m or i == n:
        divisores = __recortar(coleccion, subcoleccion)
        if len(divisores) == m and __es_divisor(min(divisores), divisores, 0):
            s[0] = s[0] + 1
    else:
        for k in range(0, 2):
            # Ramificación en el arbol, se inserta o no el candidato coleccion[i] en la solucion parcial
            subcoleccion[i] = k

            # Se expande la solucion
            if k == 0:
                subcolecciones(i + 1, coleccion, n, m, ns, subcoleccion, s)
            else:
                subcolecciones(i + 1, coleccion, n, m, ns + 1, subcoleccion, s)

            # Se deshace el candidato
            subcoleccion[i] = 0


# Devuelve una lista con los elementos de coleccion que estaban a True en solucion
# El menor de la lista debe ser divisor de todos los elementos
def __recortar(coleccion, soluciones):
    if soluciones == [] and coleccion == []:
        return []
    else:
        if soluciones[0]:
            return [coleccion[0]] + __recortar(coleccion[1:], soluciones[1:])
        else:
            return __recortar(coleccion[1:], soluciones[1:])


# Comprueba si el divisor es divisor de todos los números de la lista dividendos
def __es_divisor(divisor, dividendos, i):
    if i == len(dividendos):
        return True
    else:
        return (dividendos[i] % divisor == 0) and __es_divisor(divisor, dividendos, i + 1)


# Función iterativa para leer una lista de n números enteros
def lee_lista(n):
    a = []
    if n > 0:
        cadena_entrada = input()
        for i in range(0, n):
            elemento = int(cadena_entrada.split(" ")[i])
            a.append(elemento)

    return a


n = int(input())
coleccion = lee_lista(n)
m = int(input())

subcolecciones_principal(coleccion, n, m)
