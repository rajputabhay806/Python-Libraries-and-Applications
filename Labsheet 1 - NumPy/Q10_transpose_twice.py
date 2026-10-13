import numpy as np
matrix = np.arange(1, 10).reshape(3, 3)
transposed = matrix.T
restored = transposed.T
print("Original:\n", matrix)
print("Transpose:\n", transposed)
print("Transpose of transpose equals original:", np.array_equal(matrix, restored))
