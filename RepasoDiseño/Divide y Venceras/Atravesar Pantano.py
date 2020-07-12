import numpy as np

# Ejercicio 7.2
def Atravesar_Pantano(A, p, q):
    (f, c) = A.shape
    if p < 0 or p >= f or A[p, q] == 'W':
        return False
    elif q == c - 1:
        return A[p, q] == 'D'
    else:
        return Atravesar_Pantano(A, p, q + 1)\
               or Atravesar_Pantano(A, p - 1, q + 1)\
               or Atravesar_Pantano(A, p + 1, q + 1)

A = np.array([['W', 'W', 'W', 'W', 'W'],
              ['D', 'W', 'W', 'W', 'D'],
              ['D', 'D', 'W', 'D', 'W'],
              ['W', 'W', 'D', 'W', 'W']])
print(Atravesar_Pantano(A, 1, 0))
