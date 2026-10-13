import numpy as np
arr = np.array([10, 20, 30, 40, 50], dtype=float)
minimum, maximum = arr.min(), arr.max()
normalized = (arr - minimum) / (maximum - minimum) if maximum != minimum else np.zeros_like(arr)
print("Normalized:", normalized)
