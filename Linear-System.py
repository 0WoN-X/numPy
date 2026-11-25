
import numpy as np

A = np.array([[3, 1, -1],[2, 4, 1],[-1, 2, 5]])
B = np.array([4, 10, 2])
X = np.linalg.solve(A, B)


print("SOLUTION")
print(X)