import numpy as np

# A se divide verticalmente y B horizontalmente
def multiplicacion(A, B):
    (an, am) = A.shape
    (bn, bm) = B.shape

    if am == bn:
        # Caso Base
        # Hay que multiplicar una columna (A) por una fila (B)
        if am == 1:
            # Forma simplificada con numpy:
            # return np.multiply(A, B)

            # Forma manual
            C = np.zeros((an, bm), dtype=int)
            for i in range(an):
                for j in range(bm):
                    C[i, j] = A[i, 0] * B[0, j]
            return C

        elif an == 0 or am == 0 or bm == 0:
            return np.zeros((an, bm))

        else:
            A1 = A[0:an, 0:am//2]
            A2 = A[0:an, am//2: am]
            B1 = B[0:bn//2, 0:bm]
            B2 = B[bn//2:bn, 0:bm]

            return multiplicacion(A1, B1) + multiplicacion(A2, B2)


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
C = multiplicacion(A, B)
print("C:\n", C, "\n")

print("control:\n", np.dot(A, B))
