def subcolecciones_principal(coleccion, n, m):
    subcoleccion = []
    s = [0]
    subcolecciones(0, coleccion, n, m, 0, subcoleccion, s)
    print(s[0])


# i:            indice de la iteración
# coleccion:    vector de números
# n:            tamaño del vector de numeros
# m:            tamaño de la subcolección
# ns:           número de elementos de la subcolección
# subcoleccion: subcoleccion de elementos de la colección
# s:            número de subcolecciones de tamaño m que cumplen las restricciones, está implementado
#               como una lista de un número porque de esta forma se puede modificar el valor desde la llamada recursiva
def subcolecciones(i, coleccion, n, m, ns, subcoleccion, s):
    # Caso Base: subcolección completa
    # Si la subcoleccion tiene m elementos y el menor de ellos es el divisor de los demás, he encontrado una solución
    # Como no es necesario mostrar la solución, simplemente sumo uno a la variable s
    if ns == m or i == n:
        if len(subcoleccion) == m and __es_divisor(min(subcoleccion), subcoleccion, 0):
            s[0] = s[0] + 1
    else:
        for k in range(0, 2):
            # Se expande la solucion
            if k == 0:
                subcolecciones(i + 1, coleccion, n, m, ns, subcoleccion, s)
            else:
                subcoleccion.append(coleccion[i])
                subcolecciones(i + 1, coleccion, n, m, ns + 1, subcoleccion, s)

            if k == 1:
                # Se deshace el candidato
                subcoleccion.pop()


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
