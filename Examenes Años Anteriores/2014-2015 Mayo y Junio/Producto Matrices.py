import numpy as np

def Producto_Matrices(A, B):
    p = A.shape[0]
    q = A.shape[1]
    r = B.shape[1]

    if p == 0 or q == 0 or r == 0:
        return np.zeros((p, r))
    elif p == 1 and q == 1 and r == 1:
        return A[0, 0] * B[0, 0]
    else:
        A11 = A[0:p // 2, 0:q // 2]
        A12 = A[0:p // 2, q // 2:q]
        A21 = A[p // 2:p, 0:q // 2]
        A22 = A[p // 2:p, q // 2:q]

        B11 = B[0:q // 2, 0:r // 2]
        B12 = B[0:q // 2, r // 2:r]
        B21 = B[q // 2:q, 0:r // 2]
        B22 = B[q // 2:q, r // 2:r]

        C11 = Producto_Matrices(A11, B11) + Producto_Matrices(A12, B21)
        C12 = Producto_Matrices(A11, B12) + Producto_Matrices(A12, B22)
        C21 = Producto_Matrices(A21, B11) + Producto_Matrices(A22, B21)
        C22 = Producto_Matrices(A21, B12) + Producto_Matrices(A22, B22)

        return np.vstack([np.hstack([C11, C12]), np.hstack([C21, C22])])


A = np.array([[1, 1],
              [0, 1],
              [1, 0]])
B = np.array([[2, 1, 3, 1],
              [1, 0, 4, 2]])
"""
A = np.array([[1, 0],
              [2, 1]])
B = np.array([[2, 3],
              [1, 2]])
"""

print("A:\n", A, "\n")
print("B:\n", B, "\n")
C = Producto_Matrices(A, B)
print("C:\n", C, "\n")

print("control:\n", np.dot(A, B))