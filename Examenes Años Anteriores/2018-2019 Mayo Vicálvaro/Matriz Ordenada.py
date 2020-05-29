import numpy as np

def Matriz_Ordenada(A):
    (p, q) = A.shape
    pm = p // 2
    qm = q // 2

    if p == 0 or q == 0:
        return True
    if p == 1 and q == 1:
        return True
    else:
        filas_ordenadas = True
        for i in range(q):
            if A[pm, i] < A[pm - 1, i]:
                filas_ordenadas = False

        columnas_ordenadas = True
        for i in range(p):
            if A[i, qm] < A[i, qm - 1]:
                columnas_ordenadas = False

        A11 = A[0:pm, 0:qm]
        A12 = A[0:pm, qm:q]
        A21 = A[pm:p, 0:qm]
        A22 = A[pm:p, qm:q]

        return filas_ordenadas and columnas_ordenadas and Matriz_Ordenada(A11) and Matriz_Ordenada(A12) and Matriz_Ordenada(A21) and Matriz_Ordenada(A22)


A = np.array([[1, 2, 6, 8, 10],
              [2, 4, 7, 9, 10],
              [4, 8, 11, 14, 14],
              [5, 10, 12, 15, 16]])
print(A)
print(Matriz_Ordenada(A))
