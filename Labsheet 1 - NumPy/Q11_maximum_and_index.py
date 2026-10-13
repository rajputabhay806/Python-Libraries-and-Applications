import numpy as np
rng = np.random.default_rng()
arr = rng.integers(0, 101, size=12)
index = np.argmax(arr)
print("Array:", arr)
print("Maximum:", arr[index])
print("Index:", index)
