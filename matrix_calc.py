import numpy as np

A = np.array([[2, 1], [1, 3]])
B = np.array([[1, 2], [3, 4]])

print("A =")
print(A)
print("B =")
print(B)
print("A + B =")
print(A + B)
print("A x B =")
print(A @ B)
print("det(A) =", round(np.linalg.det(A), 2))
print("inverse of A =")
print(np.round(np.linalg.inv(A), 3))
vals, vecs = np.linalg.eig(A)
print("eigenvalues of A =", np.round(vals, 3))