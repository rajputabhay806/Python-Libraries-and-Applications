import numpy as np
arr = np.array([10, 12, 11, 13, 12, 14, 11, 100, 9], dtype=float)
mean, std = arr.mean(), arr.std()
mask = np.abs(arr - mean) <= 2 * std
print("Original:", arr)
print("Mean:", mean, "Standard deviation:", std)
print("Without values beyond 2 standard deviations:", arr[mask])
