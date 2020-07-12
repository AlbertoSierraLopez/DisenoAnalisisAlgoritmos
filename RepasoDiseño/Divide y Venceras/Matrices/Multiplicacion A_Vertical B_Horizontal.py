import numpy as np

# Ejercicio 6.7
def Multiplicacion(A, B):
    p = A.shape[0]
    q = A.shape[1]
    r = B.shape[1]

    if p == 0 or q == 0 or r == 0:
        return np.zeros((p, r))
    elif q == 1:
        return np.dot(A, B)
    else:
        A1 = A[0:p, 0:q // 2]
        A2 = A[0:p, q // 2: q]

        B1 = B[0:q // 2, 0:r]
        B2 = B[q // 2:q, 0:r]

        return Multiplicacion(A1, B1) + Multiplicacion(A2, B2)


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
