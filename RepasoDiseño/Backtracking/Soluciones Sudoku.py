# Ejercicio 12.3
import numpy as np
import math

def Soluciones_Sudoku(S, fila, columna, n_soluciones):
    if fila == 9 and columna == 0:
        print(S)
        n_soluciones += 1
    else:
        if S[fila, columna] != 0:
            (nueva_fila, nueva_columna) = Incremento(fila, columna)
            n_soluciones = Soluciones_Sudoku(S, nueva_fila, nueva_columna, n_soluciones)
        else:
            for k in range(1, 10):
                if Valido(S, fila, columna, k):
                    S[fila, columna] = k
                    (nueva_fila, nueva_columna) = Incremento(fila, columna)
                    n_soluciones = Soluciones_Sudoku(S, nueva_fila, nueva_columna, n_soluciones)
                    S[fila, columna] = 0
    return n_soluciones


def Soluciones_Sudoku_Wrapper(S):
    return Soluciones_Sudoku(S, 0, 0, 0)


def Incremento(fila, columna):
    if columna == 8:
        return (fila + 1, 0)
    else:
        return (fila, columna + 1)

def Valido(S, fila, columna, digito):
    for i in range(9):
        if i != columna and S[fila, i] == digito:
            return False

    for j in range(9):
        if j != fila and S[j, columna] == digito:
            return False

    box_row = math.floor(fila / 3)
    box_col = math.floor(columna / 3)
    for k in range(0, 3):
        for m in range(0, 3):
            if (fila != 3 * box_row + k and columna != 3 * box_col + m):
                if digito == S[3 * box_row + k][3 * box_col + m]:
                    return False
    return True


S = np.array([[0, 6, 0, 1, 0, 4, 0, 5, 0],
              [0, 0, 8, 3, 0, 5, 6, 0, 0],
              [2, 0, 0, 0, 0, 0, 0, 0, 1],
              [8, 0, 0, 4, 0, 7, 0, 0, 6],
              [0, 0, 6, 0, 0, 0, 3, 0, 0],
              [7, 0, 0, 9, 0, 1, 0, 0, 4],
              [5, 0, 0, 0, 0, 0, 0, 0, 2],
              [0, 0, 7, 2, 0, 6, 9, 0, 0],
              [0, 4, 0, 5, 0, 8, 0, 7, 0]])
print(Soluciones_Sudoku_Wrapper(S))
