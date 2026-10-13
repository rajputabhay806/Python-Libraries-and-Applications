import numpy as np
rng = np.random.default_rng()
matrix = rng.integers(10, 51, size=(3, 3))
print("Original:\n", matrix)
print("Rows sorted:\n", np.sort(matrix, axis=1))
