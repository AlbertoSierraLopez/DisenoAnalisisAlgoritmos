import numpy as np

A = np.array([[1],
              [2]])
B = np.array([[2, 3]])

print("A:\n", A)
print("B:\n", B)

print("multiply:\n", np.multiply(A, B))

print("dot A B:\n", np.dot(A, B))
print("dot B A:\n", np.dot(B, A))
