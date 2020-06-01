import numpy as np

def Knight_Tour_Wrapper(n, origenF, origenC):
    T = np.zeros((n, n))
    movimientoF = [1, 2 , 2, 1, -1, -2, -2, -1]
    movimientoC = [2, 1, -1, -2, -2, -1, 1, 2]
    T[origenF, origenC] = 1
    Knight_Tour(T, n, 2, origenF, origenC, movimientoF, movimientoC)


def Knight_Tour(T, n, i, fila, columna, movimientoF, movimientoC):
    if i > n ** 2:
        print(T)
        return True
    else:
        encontrado = False
        k = 0
        while k < 8 and not encontrado:
            nFila = fila + movimientoF[k]
            nColumna = columna + movimientoC[k]
            if nFila >= 0 and nFila < n and nColumna >= 0 and nColumna < n and T[nFila, nColumna] == 0:
                T[nFila, nColumna] = i
                encontrado = Knight_Tour(T, n, i + 1, nFila, nColumna, movimientoF, movimientoC)
                T[nFila, nColumna] = 0
            k += 1
        return encontrado



n = int(input())
x = int(input())
y = int(input())
Knight_Tour_Wrapper(n, x, y)
