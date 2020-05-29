import numpy as np
import math

def Minimo_Matriz(A):
    (n, m) = A.shape
    if n == 0 or m == 0:
        return math.inf
    elif n == 1 and m == 1:
        return A[0, 0]
    else:
        A11 = A[0:n//2, 0:m//2]
        A12 = A[0:n//2, m//2:m]
        A21 = A[n//2:n, 0:m//2]
        A22 = A[n//2:n, m//2:m]

        return min(Minimo_Matriz(A11), Minimo_Matriz(A12), Minimo_Matriz(A21), Minimo_Matriz(A22))


A = np.array([[6, 2, 3],
              [1, 8, 5],
              [9, 7, 4]])
print(A)
print(Minimo_Matriz(A))
