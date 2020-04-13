import numpy as np

def matriz_ordenada(A):
    (filas, columnas) = A.shape

    if filas == 1 and columnas == 1:
        return True
    elif filas == 0 or columnas == 0:
        return True
    else:
        filas_m = filas // 2
        columnas_m = columnas // 2
        orden = True

        i = 0
        while i < columnas - 1 and orden:
            orden = A[filas_m, i] <= A[filas_m, i + 1]
            i = i + 1

        j = 0
        while j < filas - 1 and orden:
            orden = A[j, columnas_m] <= A[j + 1, columnas_m]
            j = j + 1

        return orden and \
               matriz_ordenada(A[0:filas_m, 0:columnas_m]) and \
               matriz_ordenada(A[0:filas_m, columnas_m+1:columnas]) and \
               matriz_ordenada(A[filas_m+1:filas, 0:columnas_m]) and \
               matriz_ordenada(A[filas_m+1:filas, columnas_m+1:columnas])


M = np.array([[1, 2, 3, 4],
              [3, 4, 5, 6],
              [4, 6, 7, 8],
              [5, 8, 9, 10]])
print(M)
print("Ordenada:", matriz_ordenada(M))
