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


def __es_divisor(divisor, dividendos, i):
    if i == len(dividendos):
        return True
    else:
        return (dividendos[i] % divisor == 0) and __es_divisor(divisor, dividendos, i + 1)


n = 5
coleccion = [2, 2, 4, 5, 7]
m = 2

soluciones = [0, 1, 1, 0, 0]
divisores = __recortar(coleccion, soluciones)
print(__es_divisor(min(divisores), divisores, 0))