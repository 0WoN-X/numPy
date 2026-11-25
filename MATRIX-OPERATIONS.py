
import numpy as np

A = np.random.randint(1, 11, size=(3, 3))
B = np.random.randint(1, 11, size=(3, 3))


print("Matrix A:")
print(A)

print("\nMatrix B:")
print(B)


print("\nA x B:")
print(np.dot(A, B))


print("\nTranspose of A:")
print(A.T)


print("\nInverse of A:")
try:
    print(np.linalg.inv(A))
except np.linalg.LinAlgError:
    print("A is not invertible (determinant = 0)")
