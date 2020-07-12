import numpy as np

def Cuadrado_Magico_Wrapper(n):
    constante = n * ((n**2 + 1) / 2)
    sol_parcial = np.zeros((n, n))
    validos = [True] * (n**2)
    fila_parcial = [0] * n
    columna_parcial = [0] * n
    return Cuadrado_Magico(n, 0, 0, 0, sol_parcial, validos, constante, fila_parcial, columna_parcial, 0, 0)


def Cuadrado_Magico(n, iteracion, i, j, sol_parcial, validos, constante, fila_parcial, columna_parcial, diagonalD_parcial, diagonalI_parcial):
    if iteracion == n**2:
        if sum(fila_parcial) == constante * n and sum(columna_parcial) == constante * n and diagonalD_parcial == constante and diagonalI_parcial == constante:
            print(sol_parcial)
            return 1
        else:
            return 0
    else:
        num_soluciones = 0

        for k in range(1, n**2 + 1):
            fila_parcial[i] += k
            columna_parcial[j] += k
            if i == j:
                diagonalD_parcial += k
            if i + j == n - 1:
                diagonalI_parcial += k

            if validos[k - 1] and (fila_parcial[i] <= constante) and (columna_parcial[j] <= constante) and (diagonalI_parcial <= constante) and (diagonalD_parcial <= constante):

                sol_parcial[i, j] = k
                validos[k - 1] = False

                suc = Sucesor(n, i, j)
                num_soluciones += Cuadrado_Magico(n, iteracion + 1, suc[0], suc[1], sol_parcial, validos, constante, fila_parcial, columna_parcial, diagonalD_parcial, diagonalI_parcial)

                sol_parcial[i, j] = 0
                validos[k - 1] = True

            fila_parcial[i] -= k
            columna_parcial[j] -= k
            if i == j:
                diagonalD_parcial -= k
            if i + j == n - 1:
                diagonalI_parcial -= k

        return num_soluciones


def Sucesor(n, i, j):
    if j == n - 1:
        return [i + 1, 0]
    else:
        return [i, j + 1]


n = int(input())
print(Cuadrado_Magico_Wrapper(n))
