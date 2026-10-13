import numpy as np
arr = np.arange(1, 17)
matrix = arr.reshape(4, 4)
print("4x4 matrix:\n", matrix)
print("Transposed (rows and columns exchanged):\n", np.transpose(matrix))
