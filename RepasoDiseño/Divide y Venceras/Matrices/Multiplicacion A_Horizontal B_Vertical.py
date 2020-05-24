import numpy as np

# Ejercicio 6.8
def Multiplicacion(A, B):
    p = A.shape[0]
    q = A.shape[1]
    r = B.shape[1]

    if p == 0 or q == 0 or r == 0:
        return np.zeros((p, r))
    elif p == 1 and r == 1:
        return np.dot(A, B)
    else:
        A1 = A[0:p // 2, 0:q]
        A2 = A[p // 2:p, 0:q]

        B1 = B[0:q, 0:r // 2]
        B2 = B[0:q, r //2:r]

        C11 = Multiplicacion(A1, B1)
        C12 = Multiplicacion(A1, B2)
        C21 = Multiplicacion(A2, B1)
        C22 = Multiplicacion(A2, B2)

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
C = Multiplicacion(A, B)
print("C:\n", C, "\n")

print("control:\n", np.dot(A, B))
