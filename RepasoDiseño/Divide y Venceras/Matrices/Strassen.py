import numpy as np

# Ejercicio 6.6
def Strassen(A, B):
    p = A.shape[0]  # Las raíces son cuadradas y de la misma dimensión, que además es potencia de 2
    p2 = p // 2

    if p == 1:
        return np.array([A[0, 0] * B[0, 0]])
    else:
        A11 = A[0:p2, 0:p2]
        A12 = A[0:p2, p2:p]
        A21 = A[p2:p, 0:p2]
        A22 = A[p2:p, p2:p]

        B11 = B[0:p2, 0:p2]
        B12 = B[0:p2, p2:p]
        B21 = B[p2:p, 0:p2]
        B22 = B[p2:p, p2:p]

        M1 = Strassen(A11 + A22, B11 + B22)
        M2 = Strassen(A21 + A22, B11)
        M3 = Strassen(A11, B12 - B22)
        M4 = Strassen(A22, B21 - B11)
        M5 = Strassen(A11 + A12, B22)
        M6 = Strassen(A21 - A11, B11 + B12)
        M7 = Strassen(A12 - A22, B21 + B22)

        C11 = M1 + M4 - M5 + M7
        C12 = M3 + M5
        C21 = M2 + M4
        C22 = M1 - M2 + M3 + M6

        return np.vstack([np.hstack([C11, C12]), np.hstack([C21, C22])])


def Strassen_Wrapper(A, B):
    (p, q) = A.shape
    (q, r) = B.shape

    n = max(p, q, r)
    k = np.ceil(np.log2(n))
    k = 2 ** k

    Ap = np.pad(A, ((0, k - p), (0, k - q)), 'constant')
    Bp = np.pad(B, ((0, k - q), (0, k - r)), 'constant')

    return Strassen(Ap, Bp)


A = np.array([[1, 0],
              [2, 1]])
B = np.array([[2, 3],
              [1, 2]])

print(Strassen(A, B))
