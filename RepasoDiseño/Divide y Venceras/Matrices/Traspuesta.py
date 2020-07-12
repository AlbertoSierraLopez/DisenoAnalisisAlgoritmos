import numpy as np

# Ejercicio 6.5
def Traspuesta(A):
    n = A.shape[0]
    m = A.shape[1]

    if n == 0 or m == 0:
        return np.zeros((m, n))
    elif n == 1 and m == 1:
        return A
    else:
        A11 = Traspuesta(A[0:n // 2, 0:m // 2])
        A12 = Traspuesta(A[0:n // 2, m // 2: m])
        A21 = Traspuesta(A[n // 2:n, 0:m // 2])
        A22 = Traspuesta(A[n // 2:n, m // 2:m])

        return np.vstack([np.hstack([A11, A21]), np.hstack([A12, A22])])


A = np.array([[1, 2, 3],
              [3, 1, 2]])
print("A:\n", A)
print("T(A):\n", Traspuesta(A))
